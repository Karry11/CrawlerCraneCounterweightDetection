from ultralytics import YOLO
from PIL import Image
import numpy as np

model_path = "best.pt"
image_path = "1.jpg"
model = YOLO(model_path)

def _slice_classify(slice_list):
    dic_target = {0: 0, 1: 0, 2: 0, 3: 0}
    for slice_img, conf in slice_list:
        a = model.predict(slice_img, save=False)[0].boxes.cls.cpu().numpy()
        inference_number = a
        print(inference_number)
        if len(inference_number) < 1:
            continue
        else:
            # 针对单张子图识别出多个类别的情况进行优化，只返回子图中出现次数最多的数字
            unique_nums, counts = np.unique(inference_number, return_counts=True)
            most_frequent_index = np.argmax(counts)
            most_frequent = int(unique_nums[most_frequent_index])
            dic_target[most_frequent] += 1
    # 返回出现次数最多的数字
    return max(dic_target, key=lambda k: dic_target[k])

im1 = Image.open(image_path)
slice_img = [(im1,0.1)]
tmp = _slice_classify(slice_img)

# array = np.random.rand(640, 640, 3)
# results = model.predict(array, save=True)
print("inference endding")
