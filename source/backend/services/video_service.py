import cv2
import os

def extract_frames(video_path):
    os.makedirs("temp/frames", exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frame_paths = []
    count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        # 1 frame per second
        if count % fps == 0:
            path = f"temp/frames/frame_{count}.jpg"
            cv2.imwrite(path, frame)
            frame_paths.append(path)

        count += 1

    cap.release()
    return frame_paths