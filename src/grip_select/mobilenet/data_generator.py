import os
from pathlib import Path
from typing import Optional

import pandas as pd

import cv2
import time

from tqdm import tqdm

from src.definitions import SETTINGS, ROOT_PATH
from src.grip_select.mobilenet.analyzer import MobileNetAnalyzer, MobileNetAnalysisResult
from src.utils import BoundingBox

if __name__ == "__main__":
    input_dir_path = ROOT_PATH / SETTINGS["grip_select"]["mobilenet"]["data_dir"]
    output_dir_path = ROOT_PATH / SETTINGS["grip_select"]["mobilenet"]["results_dir"]
    train_image_dims = (50, 50)

    extensions = [".png", ".jpg", ".jpeg"]
    files = []
    for ext in extensions:
        files.extend(input_dir_path.glob("**/*" + ext))

    print("Generating training data from", len(files), "images in directory", input_dir_path)

    analyzer = MobileNetAnalyzer(confidence_threshold=0.5)

    out_results = []

    for file in tqdm(files):
        image = cv2.imread(str(file))
        results: Optional[MobileNetAnalysisResult] = analyzer.analyze_image(image)
        if not results:
            continue
        square_bbox: BoundingBox = results.bbox.squarify()

        tl_x = int(square_bbox.x)
        br_x = int(square_bbox.bottom_right.x)
        tl_y = int(square_bbox.y)
        br_y = int(square_bbox.bottom_right.y)
        crop_image = image[tl_y:br_y, tl_x:br_x]

        cropped_resized_image = cv2.resize(crop_image, train_image_dims)
        out_tuple = (cropped_resized_image.tolist(), results.class_name, results.confidence, results.grip_type)
        out_results.append(out_tuple)

    out_df = pd.DataFrame(out_results, columns=["image", "object_class", "confidence", "grip_type"])

    timestr = time.strftime("%Y%m%d_%H%M%S")
    out_filename = timestr + "_train_size_" + str(len(out_results)) + ".csv"
    out_path = str(output_dir_path / out_filename)
    out_df.to_csv(out_path)
