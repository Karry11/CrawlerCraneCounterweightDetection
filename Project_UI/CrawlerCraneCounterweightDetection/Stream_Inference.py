# This Python file uses the following encoding: utf-8

from PySide6.QtGui import QPixmap,QImage
from PySide6.QtCore import Qt, QThread, Signal
import cv2
import time
from ultralytics import YOLO
import numpy as np
from collections import deque, Counter
from knn import knn_classifier
class Stream_Inference(QThread):
    processed_image = Signal(QImage)
    result_info = Signal(int,float,float,float,str)
    def __init__(self,stream_path,weight_path,imgsz,conf,device,half,weight_sr,weight_character):
        super().__init__()
        #配重检测
        self.stream_path = stream_path
        self.weight_path = weight_path
        self.weight_character = weight_character
        self.imgsz = imgsz
        self.conf=conf
        self.device=device
        self.half=half
        self.model = YOLO(self.weight_path,task='segment')
        self.thread_stop = False
        self.label=True
        self.box = True

        #切片字符检测
        self.sr_model_flag = False
        self.sr_model = cv2.dnn_superres.DnnSuperResImpl_create()
        self.sr_model.readModel(weight_sr)
        self.sr_model.setModel("espcn", 2)
        self.model_character = YOLO(self.weight_character)
        self.model_character_dic = {0: '10t', 1: '5.1t', 2: '5t', 3: '8.1t'}

        #结果信息
        self.num_weight=5
        self.num_weight_queue = deque(maxlen=5)
        self.total_mass=10.00
        self.total_mass_L=5.00
        self.total_mass_R=5.00
        self.warming_info="安全"

    def stop(self):
        self.thread_stop = True

    def sr_model_state(self):
        self.sr_model_flag=True

    def _slice_classify(self, slice_list):
        dic_target = {0:0,1:0,2:0,3:0}
        character_pos=[]
        for slice_img, conf, int_box in slice_list:
            result = self.model_character.predict(slice_img)
            inference_number = result[0].boxes.cls.cpu().numpy()
            boxes = result[0].boxes.cpu().numpy().data
            sorted_box_list = sorted(boxes, key=lambda x: x[4], reverse=True)
            char_int_boxes =  np.floor(sorted_box_list).astype(int)
            if len(inference_number) < 1:
                continue
            else:
                #针对单张子图识别出多个类别的情况进行优化，只返回子图中出现次数最多的数字
                unique_nums, counts = np.unique(inference_number, return_counts=True)
                most_frequent_index = np.argmax(counts)
                most_frequent = int(unique_nums[most_frequent_index])
                dic_target[most_frequent] += 1
                int_box[0], int_box[1], int_box[2], int_box[3] = int_box[0]+char_int_boxes[0][0],int_box[1]+char_int_boxes[0][1],int_box[0]+char_int_boxes[0][2],int_box[1]+char_int_boxes[0][3]
                #字符位置
                character_pos.append(int_box)
        # 返回出现次数最多的数字
        return max(dic_target, key=lambda k: dic_target[k]),character_pos

    def _get_image_slice(self):
        original_image = self.result[0].orig_img
        boxes = self.result[0].boxes.cpu().numpy().data
        # 置信度
        conf_list = boxes[:, 4]
        # 对检测框参数进行向下取整
        int_boxes = np.floor(boxes).astype(int)
        img_list = []
        for i in range(int_boxes.shape[0]):
            x1, y1, x2, y2 = int_boxes[i][0], int_boxes[i][1], int_boxes[i][2], int_boxes[i][3]
            img_i = original_image[y1:y2 + 1, x1:x2 + 1]
            # 如果需要进行超分辨里增强的话，则调用sr_model完成上采样操作（默认放大因子为2）
            if self.sr_model_flag:
                img_i = self.sr_model.upsample(img_i)
            img_list.append((img_i,conf_list[i],int_boxes[i]))
        return img_list

    def run(self):
        cap = cv2.VideoCapture(self.stream_path)
        #未捕获video
        if not cap.isOpened():
            self.num_weight,self.total_mass,self.total_mass_L,self.total_mass_R,self.warming_info = 0,0,0,0,"视频流中断，请检查网络相机连接情况"
            self.result_info.emit(self.num_weight,self.total_mass,self.total_mass_L,self.total_mass_R,self.warming_info)
            cap.release()
            return
        fps = cap.get(cv2.CAP_PROP_FPS)
        delta_time=1000/fps
        while cap.isOpened() and not self.thread_stop:
            start_time = time.time()
            ret, frame = cap.read()
            if ret:
                self.result = self.model(frame,imgsz=self.imgsz,conf=self.conf,half=self.half ,device=self.device,vid_stride = 3)
                # 通过预测狂和原始图像数据得到切片图像，通过对切片图像完成超分辨率增强后输出结果 [(图像切片1，置信度1),(图像切片2， 置信度2).....]
                slice_result = self._get_image_slice()
                classify_number,character_pos = self._slice_classify(slice_result)
                annotated_image = self.result[0].plot(conf=True,line_width=2,font_size=None,font="Arial.ttf",pil=False,img=None,im_gpu=None,kpt_radius=5,
                            kpt_line=True,labels=self.label,boxes=self.box,masks=False,probs=True,show=False,save=False,filename=None)
                for box in character_pos:
                    cv2.rectangle(annotated_image, (box[0], box[1]), (box[2], box[3]),  color=(0,0,255), thickness=2)
                rgb_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qimage = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                # 将检测结果添加到队列中
                self.num_weight_queue.append(len(self.result[0].boxes))
                # 获取队列中元素的统计信息
                counter = Counter(self.num_weight_queue)
                # 获取出现次数最多的元素（众数）
                self.num_weight = counter.most_common(1)[0][0]
                # 计算左右两边配重块数和重量
                boxes_number = self.result[0].boxes.cpu().numpy().data
                int_boxes_number = np.floor(boxes_number).astype(int)
                self.weight_left_number, self.weight_right_number = knn_classifier(int_boxes_number)
                self.total_mass_L = self.weight_left_number * float(eval(self.model_character_dic[classify_number][0:-1]))
                self.total_mass_R = self.weight_right_number * float(
                    eval(self.model_character_dic[classify_number][0:-1]))
                # 计算完之后对左右数量置为0，避免带入缓存误差
                self.weight_left_number, self.weight_right_number = 0, 0

                self.processed_image.emit(qimage)
                self.total_mass = self.num_weight * float(eval(self.model_character_dic[classify_number][0:-1]))
                self.result_info.emit(self.num_weight,self.total_mass,self.total_mass_L,self.total_mass_R,self.warming_info)

            else:
                break
            end_time = time.time()
            processing_time = (end_time-start_time)*1000
            print(processing_time)
            if processing_time>delta_time:
                continue
            else:
                cv2.waitKey(int(delta_time-processing_time))
        #中途中断
        if not cap.isOpened():
            self.warming_info = "视频流中断，请检查网络相机连接情况"
            self.num_weight,self.total_mass,self.total_mass_L,self.total_mass_R = 0,0,0,0
            self.result_info.emit(self.num_weight,self.total_mass,self.total_mass_L,self.total_mass_R,self.warming_info)
        cap.release()
