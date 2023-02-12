import argparse
import sys
from pathlib import Path

from src.grasp_analytics.definitions import ROOT_PATH
from grasp_analytics.modules.fsr_matrix.classifier.matrix_classifier import MatrixClassifier
# import classifier.matrix_classifier.MatrixClassifier
from grasp_analytics.modules.fsr_matrix.data_processing.reader_file import FileReader
from grasp_analytics.modules.fsr_matrix.data_processing.reader_uart import UartReader
from grasp_analytics.modules.fsr_matrix.data_processing.reader_pipe import PipeReader
from grasp_analytics.modules.fsr_matrix.visualizer import MatrixVisualizer

parser = argparse.ArgumentParser(description="Visualize FSR data in real time")
parser.add_argument(
    "--file",
    type=str,
    default=None,
    help="Read from a file with a specified path relative to the root directory",
)
parser.add_argument(
    "--file_absolute_path",
    type=str,
    default=None,
    help="Read from a file with a specified absolute path",
)
parser.add_argument(
    "--port",
    type=str,
    default=None,
    help="Read from a serial connection with a specified port",
)
parser.add_argument(
    "--pipe", type=bool, default=False, help="Read data from stdin"
)
parser.add_argument(
    "--classify", type=bool, default=False, help="Display shape classification"
)

args = parser.parse_args()

if args.port is not None:
    _reader = UartReader(port=args.port)
elif args.file_absolute_path is not None:
    _reader = FileReader(Path(args.file_absolute_path))
elif args.file is not None:
    _reader = FileReader(ROOT_PATH / args.file)
elif args.pipe:
    _reader = PipeReader()
else:
    raise Exception("No input method specified")

visualizer = MatrixVisualizer()
if args.classify:
    _classifier = MatrixClassifier()
    visualizer.start(_reader, _classifier)
else:
    visualizer.start(_reader)
