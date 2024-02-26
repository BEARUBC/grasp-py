"""
This was modified from code was written by The Computer Vision Engineer.

His github has this code as well as other scripts:
https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide/tree/master

This is his youtube video from which I learned to work with yolov8: 
https://www.youtube.com/watch?v=m9fH9OWn8YM&t=2s
"""

import os
import shutil


DATA_ALL_DIR = os.path.join(".", "raw_data")

DATA_OUT_DIR = os.path.join(".", "data")

for set_ in ["images", "labels"]:
    for dir_ in [
        os.path.join(DATA_OUT_DIR, set_),
        os.path.join(DATA_OUT_DIR, set_, "test"),
        os.path.join(DATA_OUT_DIR, set_, "train"),
        os.path.join(DATA_OUT_DIR, set_, "validation"),
    ]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.mkdir(dir_)

class_id = "/m/0pcr"

train_bboxes_filename = os.path.join(".", "oidv6-train-annotations-bbox.csv")
validation_bboxes_filename = os.path.join(".", "validation-annotations-bbox.csv")
test_bboxes_filename = os.path.join(".", "test-annotations-bbox.csv")


for j, filename in enumerate(
    [train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]
):
    set_ = ["train", "validation", "test"][j]
    print(filename)
    with open(filename, "r") as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(",")[:13]
            if class_name in [class_id]:
                if not os.path.exists(
                    os.path.join(DATA_OUT_DIR, "images", set_, "{}.jpg".format(id))
                ):
                    shutil.copy(
                        os.path.join(DATA_ALL_DIR, "{}.jpg".format(id)),
                        os.path.join(DATA_OUT_DIR, "images", set_, "{}.jpg".format(id)),
                    )
                with open(
                    os.path.join(DATA_OUT_DIR, "labels", set_, "{}.txt".format(id)), "a"
                ) as f_ann:
                    # class_id, xc, yx, w, h
                    x1, x2, y1, y2 = [float(j) for j in [x1, x2, y1, y2]]
                    xc = (x1 + x2) / 2
                    yc = (y1 + y2) / 2
                    w = x2 - x1
                    h = y2 - y1

                    f_ann.write("0 {} {} {} {}\n".format(xc, yc, w, h))
                    f_ann.close()

            line = f.readline()
