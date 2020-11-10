import argparse

from src.definitions import ROOT_PATH
from src.fsr_matrix.classifier.matrix_classifier import MatrixClassifier
from src.fsr_matrix.data_processing.reader_file import FileReader
from src.fsr_matrix.data_processing.reader_uart import UartReader
from src.fsr_matrix.visualizer import MatrixVisualizer

parser = argparse.ArgumentParser(description="Visualize FSR data in real time")
parser.add_argument("--file", type=str, default=None,
                    help="Read from a file with a specified path relative to the root directory")
parser.add_argument("--port", type=str, default=None,
                    help="Read from a serial connection with a specified port")

args = parser.parse_args()

if args.port is not None:
    _reader = UartReader(port=args.port)
elif args.file is not None:
    _reader = FileReader(ROOT_PATH / args.file)
else:
    raise Exception("No input method specified")

_classifier = MatrixClassifier()
visualizer = MatrixVisualizer()

visualizer.start(_reader, _classifier)
