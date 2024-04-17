##pip install -U ultralytics sahi
from sahi import AutoDetectionModel
from sahi.predict import  get_sliced_prediction
from IPython.display import Image

# Download YOLOv8 model
yolov8_model_path =  "./runs/detect/train/weights/best.pt"
detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov8',
    model_path=yolov8_model_path,
    confidence_threshold=0.3,
    device="cuda:0",  # or 'cuda:0'
)

result = get_sliced_prediction(
    "datasets/dataset1/train/images/frame_0_1_jpg.rf.b4ca82995975eafa2aafb270c8531623.jpg",
    detection_model,
    slice_height=256,
    slice_width=256,
    overlap_height_ratio=0.2,
    overlap_width_ratio=0.2
)
result.export_visuals(export_dir="demo_data/")
Image("demo_data/prediction_visual.png")