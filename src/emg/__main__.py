import argparse
import pandas
from src.emg.peak_detection import PeakDetection
import numpy as np

# lst = np.random.rand(50)
# peak_detector = PeakDetection(5, 2, 0.1)
#
# peak_detector.threshold_new_val(2)
# peak_detector.threshold_new_val(1)
# peak_detector.threshold_new_val(20)
#
# print(peak_detector.signals)


parser = argparse.ArgumentParser(description="Peak Detection in EMG data in real time")
parser.add_argument("--file", type=str, default=None,
                    help="Read from a file with a specified path relative to the root directory")
parser.add_argument("--file_absolute_path", type=str, default=None,
                    help="Read from a file with a specified absolute path")

args = parser.parse_args()

if args.file_absolute_path is not None:
    newValues = pandas.read_csv(args.file_absolute_path)
    peak_detector = PeakDetection(5, 2, 0.1)
    for i in newValues:
        peak_detector.threshold_new_val(i)
    print(peak_detector.signals)

elif args.file is not None:
    newValues = pandas.read_csv(args.file)
    peak_detector = PeakDetection(5, 2, 0.1)
    for i in newValues:
        peak_detector.threshold_new_val(i)
    print(peak_detector.signals)

else:
    raise Exception("No input method specified")


