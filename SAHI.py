##pip install -U ultralytics sahi
from sahi import AutoDetectionModel
from sahi.predict import  get_sliced_prediction
from IPython.display import Image

# Download YOLOv8 model
yolov8_model_path =  "./runs/detect/train/weights/best.pt"
detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov8',
    model_path=yolov8_model_path,
    confidence_threshold=0.8,
    device="cuda:0",  # or 'cuda:0'
)
source_path = "datasets/dataset1/test/images/frame_72_jpg.rf.85c0bb6b643089f373f86f874acda725.jpg"
result = get_sliced_prediction(
    source_path,
    detection_model,
    slice_height=256,
    slice_width=256,
    overlap_height_ratio=0.2,
    overlap_width_ratio=0.2
)
file_name = source_path.rsplit('/', 1)[-1]
result.export_visuals(export_dir="runs/sahi_detect/")
Image("run/sahi_detect/{}".format(file_name))