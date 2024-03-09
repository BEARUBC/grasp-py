import os
from ultralytics import YOLO
import cv2

#################
# Variables
#################

# Load a model
model = YOLO('./model/yolov8n-oiv7.pt')  # load a custom model

# List of Acceptable Object
objects = [19, 26, 322]
values = ["Haha", "Hihi", "Huhu"]

# HashMap
hashmap = dict(zip(objects, values))

#################
threshold = 0.5
#################

video = cv2.VideoCapture(0)
fullscreenState = False

while True:
    ret, frame = video.read()
    #frame = cv2.resize(ret, 640, 480)
    results = model(frame)[0]
    (h, w) = frame.shape[:2]

    if not ret:
        break

    # Check if Detected Objects are Acceptable, if yes, pick the first one.
    drawBox = False
    no_of_detected_objects = len(results.boxes.data.tolist())
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if int(class_id) in objects:
            drawBox = True

    #if drawBox:
        # smth else
        # smth
    
    # Drawbox
    cv2.putText(frame, "GRIP TYPE:", (0, 110), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

    # Choose Grip Type
    # ...

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        print(class_id)

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    key = cv2.waitKey(1) & 0xFF

    cv2.namedWindow('GRASP', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('GRASP', cv2.WINDOW_NORMAL, cv2.WINDOW_NORMAL)
    cv2.resizeWindow('GRASP', int(1920/2), int(1080/2))

    cv2.imshow('GRASP', frame)
    if key == 27:
        cv2.destroyAllWindows()
        break

    # del frame, video
video.release()