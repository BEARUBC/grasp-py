from argparse import ArgumentParser
from pathlib import Path
from fsr_matrix.classifier.matrix_classifier import MatrixClassifier
import yaml

settings_path = Path("../settings.yaml")
with open(settings_path, "r") as settings_file:
    settings = yaml.load(settings_file, Loader=yaml.FullLoader)

matrix_classifier = MatrixClassifier(settings)
