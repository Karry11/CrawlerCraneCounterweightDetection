#获取视频帧
import cv2
import os

def extract_frames(video_path, output_dir, num_frames=100):
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 打开视频文件
    video_capture = cv2.VideoCapture(video_path)
    print("视频是否打卡{}？".format(video_capture.isOpened))
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    print("总帧数{}？".format(total_frames))
    # 确定每个间隔多少帧取一次
    frame_interval = total_frames // num_frames

    # 初始化计数器
    frame_count = 0
    saved_count = 0

    # 逐帧读取视频
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # 每隔frame_interval帧保存一帧
        if frame_count % frame_interval == 0:
            output_path = os.path.join(output_dir, f"frame_{saved_count}.jpg")
            cv2.imwrite(output_path, frame)
            saved_count += 1

        frame_count += 1

    # 释放资源
    video_capture.release()

    print(f"成功保存了 {saved_count} 张帧.")

if __name__ == "__main__":
    # 输入视频文件路径
    video_path ="video_data\超起配重3月8日.mp4"

    # 输出帧的保存目录
    output_dir = "output_frames"

    # 提取帧
    extract_frames(video_path, output_dir, num_frames=100)
