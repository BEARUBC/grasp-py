import os
from pathlib import Path

import cv2
from tqdm import tqdm

from src.definitions import SETTINGS, ROOT_PATH
from src.grip_select.mobilenet.analyzer import MobileNetAnalyzer

if __name__ == "__main__":
    input_dir_path = ROOT_PATH / SETTINGS["grip_select"]["mobilenet"]["data_dir"]
    output_dir_path = str(ROOT_PATH / SETTINGS["grip_select"]["mobilenet"]["results_dir"])


    extensions = [".png", ".jpg", ".jpeg"]
    files = []
    for ext in extensions:
        files.extend(input_dir_path.glob("**/*" + ext))

    print("Generating training data from", len(files), "images in directory", input_dir_path)

    analyzer = MobileNetAnalyzer()

    for file in tqdm(files):
        image = cv2.imread(str(file))
        results = analyzer.analyze_image(image)




