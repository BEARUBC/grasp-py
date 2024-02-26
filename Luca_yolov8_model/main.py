"""

To test the model, you can either run this script for images,
or you can type the following command in the terminal:

yolo detect predict model=./runs/detect/train3/weights/last.pt source=./data/images/test/0a5e8d559aa5d680.jpg

-   you can replace train3 for your desired model to run
-   you can replace the source to be whatever image or video
    you want to test as long as the filepath is specified

"""

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
model.train(data="config.yaml", epochs=1)  # train the model
