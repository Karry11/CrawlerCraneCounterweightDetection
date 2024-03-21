import albumentations as A
import cv2
from albumentations.pytorch import ToTensorV2
import numpy as np
import pycocotools.mask as mask_utils

# 定义数据增强管道
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomContrast(limit=0.2, p=0.5),
    A.VerticalFlip(p=0.5),
    A.Resize(height=512, width=512),
    ToTensorV2()
], additional_targets={'label': 'mask'})

# 读取图像
image = cv2.imread('path_to_your_image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 示例
coco_annotation = {
    'segmentation': [[0, 0, 1, 0, 1, 1, 0, 1]],  # 这个例子表明标注形式是多边形
    'bbox': [0, 0, 1, 1],
    'category_id': 1
}

# 将COCO格式的多边形标签转换为掩码
mask = mask_utils.decode([coco_annotation['segmentation']])

# 应用增强
transformed = transform(image=image, label=mask)

transformed_image = transformed['image']
transformed_label = transformed['label']  # 如果图像需要resize，则标签也会被resize

# 增强后的结果需要保存为COCO格式的分割信息

# 保存图像
transformed_image_path = 'path_to_save_transformed_image.jpg'
cv2.imwrite(transformed_image_path, transformed_image)

# 保存掩码
transformed_label_path = 'path_to_save_transformed_label.png'
cv2.imwrite(transformed_label_path, transformed_label)

# 导出掩码为COCO的分割格式
transformed_label_coco = mask_utils.encode(np.asfortranarray(transformed_label))
