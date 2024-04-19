##pip install -U ultralytics sahi
from sahi import AutoDetectionModel
from sahi.predict import  get_sliced_prediction

# Download YOLOv8 model
yolov8_model_path =  "./runs/detect/train12/weights/best.pt"
#yolov8_model_path =  "D:/Download/best.pt"
detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov8',
    model_path=yolov8_model_path,
    confidence_threshold=0.8,
    device="cuda:0",  # or 'cuda:0'
)
source_path = "datasets/dataset2/test/images/frame_0_0_jpg.rf.05588c0bc2bd0b146fcf05ccfd975add.jpg"
result = get_sliced_prediction(
    source_path,
    detection_model,
    slice_height=256,
    slice_width=256,
    overlap_height_ratio=0.2,
    overlap_width_ratio=0.2,
    verbose=2
)
file_name = source_path.rsplit('/', 1)[-1]
result.export_visuals(export_dir="runs/sahi_detect/",file_name=file_name)
