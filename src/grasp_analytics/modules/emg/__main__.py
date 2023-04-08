import argparse
from pathlib import Path
from emg_parser import EMGParser
from peak_detector import PeakDetector
from continuous_model import ContinuousEMGModel

import pandas as pd

import plotly.express as px

from src.grasp_analytics.definitions import DATA_PATH

def main(data_path: Path, limit=2000):
    iterations = 0
    data_parser = EMGParser(data_path)  # Initialize Parser
    peak_detector = PeakDetector(20, 6000, 0.9, 4)  # Initialize Peak detector
    cont_model = ContinuousEMGModel()  # Initialize continuous model
    peaks = dict()  # Store signals in dict with (index: signal)
    data = dict()
    while data_parser.available and iterations < limit:  # Read all data in file
        iterations += 1  # Limit iterations
        reading_row = data_parser.get_reading()  # Get current reading
        reading = reading_row.iloc[0][reading_row.columns[0]]
        signal = peak_detector.threshold_new_val(
            reading
        )  # Get filtered signal from reading
        peaks[data_parser.counter] = signal  # Store signal in dictionary
        data[data_parser.counter] = reading  # Store readings for comparison

    reading_df = pd.Series(data, name="signal").to_frame()  # Readings as pandas df
    reading_df["type"] = "Reading"

    model_df = cont_model.apply_model_to_df(reading_df["signal"])
    for row in model_df.iterrows():
        cont_model.add_to_cache(row[1])
    model_df["type"] = "Model"
    model_df["signal"] = model_df["y"]

    emg_signal_df = pd.Series(peaks, name="signal").to_frame()  # peaks as pandas df
    emg_signal_df["type"] = "Peaks"

    emg_df = pd.concat([reading_df, model_df], axis=0)
    fig = px.line(emg_df, y="signal", color="type")
    fig.write_html("emg_fig.html", auto_open=True)

    emg_df = pd.concat([emg_signal_df], axis=0)
    fig = px.line(emg_df, y="signal", color="type")
    fig.write_html("peaks_fig.html", auto_open=True)


# parser = argparse.ArgumentParser(description="Peak Detection in EMG data in real time")
# parser.add_argument(
#     "--file", type=str, default=None, help="Read from a file with a specified path"
# )
#
# args = parser.parse_args()

# if args.file is not None:
#     main(DATA_PATH / Path(args.file))
# else:
#     raise Exception("No file specified")

main((DATA_PATH / "datarun1.txt"))