import pandas
import pathlib
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"


class EMGParser:
    pass


ROOT_PATH = pathlib.Path(__file__).resolve().parent
index_df = pandas.read_csv(ROOT_PATH/"raw_emg_data_unprocessed/index_finger_motion_raw.csv", encoding='utf-8')

index_df.columns = ["electrode_" + str(i+1) for i in range(len(index_df.columns))]

for col in index_df.columns:
    index_df[col] = index_df[col]**2

electrode_fig_1 = px.line(index_df, y=index_df.columns[0], title="Electrode 1 Graph (index)")
#electrode_fig_2 = px.line(index_df, y=index_df.columns[0], title="Electrode 2 Graph (index)")
##electrode_fig_3 = px.line(index_df, y=index_df.columns[0], title="Electrode 3 Graph (index)")

electrode_fig_1.show()
