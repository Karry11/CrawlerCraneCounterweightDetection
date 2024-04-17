# This Python file uses the following encoding: utf-8

from PySide6.QtGui import QPixmap,QImage
from PySide6.QtCore import Qt, QThread, Signal
import cv2
import time
from ultralytics import YOLO
class Stream_Inference(QThread):
    processed_image = Signal(QImage)
    def __init__(self,stream_path,weight_path,imgsz,conf,device,half):
        super().__init__()
        self.stream_path = stream_path
        self.weight_path = weight_path
        self.imgsz = imgsz
        self.conf=conf
        self.device=device
        self.half=half
        self.model = YOLO(self.weight_path)

    def run(self):
        cap = cv2.VideoCapture(self.stream_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        delta_time=1000/fps
        while cap.isOpened():
            start_time = time.time()
            ret, frame = cap.read()
            if ret:
                result = self.model(frame,imgsz=self.imgsz,conf=self.conf,half=self.half ,device=self.device)
                annotated_image = result[0].plot(conf=True,line_width=None,font_size=None,font="Arial.ttf",pil=False,img=None,im_gpu=None,kpt_radius=5,
                            kpt_line=True,labels=True,boxes=True,masks=True,probs=True,show=False,save=False,filename=None,)
                rgb_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                qimage = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.processed_image.emit(qimage)
            else:
                break
            end_time = time.time()
            processing_time = start_time-end_time
            if processing_time>delta_time:
                continue
            else:
                cv2.waitKey(int(delta_time-processing_time))
        cap.release()
