数据集创建与增强
step1:原始数据集获取
    运行脚本getframe.py,获取视频帧中若干帧数据。
    usage: getframe.py [-h] [--video_path VIDEO_PATH] [--num_frames NUM_FRAMES] [--output_dir OUTPUT_DIR]

step2：使用roboflow对原始数据进行打标，输出voc格式annotations（主要为了后续转换方便，暂时只找到对xml格式annotation自动生成的脚本，如有txt格式自动生成脚本可直接输出txt格式annotation）

step3：使用python 第三方库imgaug进行数据增强
    安装：pip install imgaug
    使用：参考imgaug.py

step4:将转换后的数据和标注整理，导入到roboflow，检查标签是否正确，检查无误输出dataset，标注格式为txt（yolov8）。

