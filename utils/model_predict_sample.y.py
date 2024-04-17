"""
author: <Melo>
date: <20240416>
function:<model usage>
"""
import numpy as np


# 通过预测狂和原始图像数据得到切片图像，通过对切片图像完成超分辨率增强后输出结果 [(图像切片1，置信度1),(图像切片2， 置信度2).....]
def _get_image_slice(predict_result,  sr_model=None,super_resolution=False):
    original_image = predict_result[0].orig_img
    boxes = predict_result[0].boxes.cpu().numpy().data
    # 置信度
    conf_list = boxes[:,4]

    # 对检测框参数进行向下取整
    int_boxes = np.floor(boxes).astype(int)
    img_list=[]
    for i in range(int_boxes.shape[0]):
        x1,y1,x2,y2 = int_boxes[i][0],int_boxes[i][1],int_boxes[i][2],int_boxes[i][3]
        img_i = original_image[y1:y2+1,x1:x2+1]
        #如果需要进行超分辨里增强的话，则调用sr_model完成上采样操作（默认放大因子为2）
        if super_resolution:
            img_i = sr_model.upsample(img_i)
        img_list.append((img_i,conf_list[i]))
    return img_list


# 图像推理、超分辨率增强、输出图像切片
if __name__ == '__main__':
    from ultralytics import YOLO
    from PIL import Image
    model_path = "best.pt"
    image_path = "1.jpg"
    model = YOLO(model_path)

    im1 = Image.open(image_path)
    results = model.predict(source=im1, save=True)

    import cv2
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr_model_path = "ESPCN_x2.pb"
    sr.readModel(sr_model_path)
    sr.setModel("espcn", 2)

    image_slices_list = _get_image_slice(results, sr, super_resolution=True)
    print(image_slices_list)





