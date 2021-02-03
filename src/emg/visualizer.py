import argparse
import pathlib
from datetime import datetime

import plotly.express as px
import plotly.io as pio

import pandas as pd
# pio.renderers.default = "browser"

# class EMGVisualizer:
#
#     def __init__(self):

import py

from plotly.subplots import make_subplots
from pygments.lexers import go
from pathlib import Path
from src.emg.parser import EMGParser, args, emg_parser, parser
import numpy as np

fig = make_subplots(
    rows = 4, cols = 6,
    specs=[
            [{ "rowspan": 3, "colspan": 6}, None, None, None, None, None ],
            [    None, None, None, None, None, None],
            [    None, None, None, None, None, None],
            [    {"type": "indicator"}, {"type": "indicator"}, {"type": "indicator"} , None, None, None],
          ]
)

parser=argparse.ArgumentParser(description="Parse EMG Data")
parser.add_argument("file", type=str, help="Read from a file with a specified path")
args = parser.parse_args()
emg_parser = EMGParser(pathlib.Path(args.file))
data_df = emg_parser.get_all()
y = list(data_df["electrode_1"])
x = np.arange(len(y))

fig.add_trace(
    go.Scatter(
        x=x, y=y,
        name="electrode 1",
        line_color='rgba(255,255,255,0)'
    )
)


# fig.add_trace(
#     go.Indicator(
#         mode="number",
#         # value=total_confirmed,
#         # title="Confirmed Cases",
#     ),
#     row=3, col=1
# )
#
# fig.add_trace(
#     go.Indicator(
#         mode="number",
#         # value=total_recovered,
#         # title="Recovered Cases",
#     ),
#     row=3, col=2
# )
#
# fig.add_trace(
#     go.Indicator(
#         mode="number",
#         # value=total_deaths,
#         # title="Deaths Cases",
#     ),
#     row=3, col=3
# )

fig.write_html('emg_live_visualization.html', auto_open=True)

# import plotly.plotly as py # plotly library
# from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects
# import time # timer functions
# import readadc # helper functions to read ADC from the Raspberry Pi
#
# username = 'bearubc'
# api_key =
# stream_token =
#
# py.sign_in(username, api_key)
#
# #initialize graph
#
# sensor_pin = 0
#
# readadc.initialize()
#
# stream = py.Stream(stream_token)
# stream.open()
#
# while True:
# 	sensor_data = readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
# 	stream.write({'x': datetime.datetime.now(), 'y': sensor_data})
# 	time.sleep(0.1) # delay between stream posts
#


