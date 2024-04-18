from ultralytics import YOLO
from PIL import Image
import numpy as np
model_path = "best.pt"
image_path = "1.jpg"
model = YOLO(model_path)

#im1 = Image.open(image_path)
#results = model.predict(source=im1, save=True)

array = np.random.rand(640, 640, 3)
results = model.predict(array, save=True)
print("inference endding")