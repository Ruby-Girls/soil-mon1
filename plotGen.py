import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

df = pd.read_csv("/home/pi/soil-mon1/node_red_mon_data.txt")

print(df)


fig = go.Figure()

fig.add_trace(go.Scatter(x=df.Date, y=df['Soil2'], name="Soil2", line_color='blue'))

fig.update_layout(title_text='Soil moisture 2')


plotly.offline.plot(fig,
                    filename='/home/pi/soil-mon1/soilPlot2.html',
                    auto_open=False)

print("graph plotted")
