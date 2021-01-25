from datetime import datetime

import plotly.express as px
import plotly.io as pio
# pio.renderers.default = "browser"


# class EMGVisualizer:
#
#     def __init__(self):

import py

from plotly.subplots import make_subplots
from pygments.lexers import go

fig = make_subplots(
    rows = 4, cols = 6,
    specs=[
        #apparently line is not a subplot type
            [{"type": "line", "rowspan": 3, "colspan": 6}, None, None, None, None, None ],
            [    None, None, None, None, None, None],
            [    None, None, None, None, None, None],
            [    {"type": "indicator"}, {"type": "indicator"}, {"type": "indicator"} , None, None, None],
          ]
)
#how to make line subplot? Same as in main?

fig.add_trace(
    go.Indicator(
        mode="number",
        # value=total_confirmed,
        # title="Confirmed Cases",
    ),
    row=3, col=1
)

fig.add_trace(
    go.Indicator(
        mode="number",
        # value=total_recovered,
        # title="Recovered Cases",
    ),
    row=3, col=2
)

fig.add_trace(
    go.Indicator(
        mode="number",
        # value=total_deaths,
        # title="Deaths Cases",
    ),
    row=3, col=3
)

fig.write_html('emg_live_visualization.html', auto_open=True)


#real time streaming?? install didn't work
import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects
import time # timer functions
import readadc # helper functions to read ADC from the Raspberry Pi

username = 'bearubc'
api_key = 'FSGozuQiMf7sobU30Lil'
stream_token = '70ux6z64fw'

py.sign_in(username, api_key)

#initialize graph

sensor_pin = 0

readadc.initialize()

stream = py.Stream(stream_token)
stream.open()

while True:
	sensor_data = readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
	stream.write({'x': datetime.datetime.now(), 'y': sensor_data})
	time.sleep(0.1) # delay between stream posts



