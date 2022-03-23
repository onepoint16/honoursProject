import cv2
import os

def getFrames(video_path, frames_dir):
    cap = cv2.VideoCapture(video_path)
    i = 0
    while cap.isOpened():
        ret, image = cap.read()
        if ret == False:
            break
        cv2.imwrite(os.path.join(frames_dir, str(i) + ".jpg"), image)
        i += 1
    cap.release()
    cv2.destroyAllWindows()