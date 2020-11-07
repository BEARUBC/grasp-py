from src.emg.peak_detection import PeakDetection
import numpy as np

lst = np.random.rand(50)
peak_detector = PeakDetection(5, 2, 0.1)

peak_detector.threshold_new_val(2)
peak_detector.threshold_new_val(1)
peak_detector.threshold_new_val(20)

print(peak_detector.signals)



