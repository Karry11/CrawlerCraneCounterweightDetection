# This Python file uses the following encoding: utf-8

from PySide6.QtGui import QPixmap,QImage
from PySide6.QtCore import Qt, QThread, Signal
import cv2
import time
from ultralytics import YOLO
import numpy as np
from collections import deque, Counter
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
        self.model = YOLO(self.weight_path)
        self.thread_stop = False
        self.mask=True
        self.label=True
        self.box = True

        #切片字符检测
        self.sr_model_flag = False
        self.sr_model = cv2.dnn_superres.DnnSuperResImpl_create()
        self.sr_model.readModel(weight_sr)
        self.sr_model.setModel("espcn", 2)
        self.model_character = YOLO(self.weight_character)

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

    def _get_image_slice(predict_result, sr_model=None, super_resolution=True):
        try:
            original_image = predict_result[0].orig_img
        except:
            return []
        boxes = predict_result[0].boxes.cpu().numpy().data
        # 置信度
        conf_list = boxes[:, 4]

        # 对检测框参数进行向下取整
        int_boxes = np.floor(boxes).astype(int)
        img_list = []
        for i in range(int_boxes.shape[0]):
            x1, y1, x2, y2 = int_boxes[i][0], int_boxes[i][1], int_boxes[i][2], int_boxes[i][3]
            img_i = original_image[y1:y2 + 1, x1:x2 + 1]
            # 如果需要进行超分辨里增强的话，则调用sr_model完成上采样操作（默认放大因子为2）
            if super_resolution:
                img_i = sr_model.upsample(img_i)
            img_list.append((img_i, conf_list[i]))
        return img_list

    def run(self):
        cap = cv2.VideoCapture(self.stream_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        delta_time=1000/fps
        while cap.isOpened() and not self.thread_stop:
            start_time = time.time()
            ret, frame = cap.read()
            if ret:
                result = self.model(frame,imgsz=self.imgsz,conf=self.conf,half=self.half ,device=self.device)
                # 通过预测狂和原始图像数据得到切片图像，通过对切片图像完成超分辨率增强后输出结果 [(图像切片1，置信度1),(图像切片2， 置信度2).....]
                slice_result = self._get_image_slice(result, self.sr_model)
                annotated_image = result[0].plot(conf=True,line_width=2,font_size=None,font="Arial.ttf",pil=False,img=None,im_gpu=None,kpt_radius=5,
                            kpt_line=True,labels=self.label,boxes=self.box,masks=self.mask,probs=True,show=False,save=False,filename=None,)
                rgb_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qimage = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                # 将检测结果添加到队列中
                self.num_weight_queue.append(len(result[0].boxes))
                # 获取队列中元素的统计信息
                counter = Counter(self.num_weight_queue)
                # 获取出现次数最多的元素（众数）
                self.num_weight = counter.most_common(1)[0][0]
                self.processed_image.emit(qimage)
                self.result_info.emit(self.num_weight,self.total_mass,self.total_mass_L,self.total_mass_R,self.warming_info)
            else:
                break
            end_time = time.time()
            processing_time = start_time-end_time
            if processing_time>delta_time:
                continue
            else:
                cv2.waitKey(int(delta_time-processing_time))
        cap.release()
