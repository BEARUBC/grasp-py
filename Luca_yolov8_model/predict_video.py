"""

All of this code was written by The Computer Vision Engineer.

His github has this code as well as other scripts:
https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide/tree/master

This is his youtube video from which I learned to work with yolov8: 
https://www.youtube.com/watch?v=m9fH9OWn8YM&t=2s



To test the model, you can either run this script for video,
or you can type the following command in the terminal:

yolo detect predict model=./runs/detect/train3/weights/last.pt source=./videos/alpaca1.mp4

-   you can replace train3 for your desired model to run
-   you can replace the source to be whatever image or video
    you want to test as long as the filepath is specified

"""

import os

from ultralytics import YOLO
import cv2


VIDEOS_DIR = os.path.join(".", "videos")

video_path = os.path.join(VIDEOS_DIR, "alpaca1.mp4")
video_path_out = "{}_out.mp4".format(video_path)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(
    video_path_out,
    cv2.VideoWriter_fourcc(*"MP4V"),
    int(cap.get(cv2.CAP_PROP_FPS)),
    (W, H),
)

model_path = os.path.join(".", "runs", "detect", "train3", "weights", "last.pt")

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.5

while ret:

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(
                frame,
                results.names[int(class_id)].upper(),
                (int(x1), int(y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.3,
                (0, 255, 0),
                3,
                cv2.LINE_AA,
            )

    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()
