import plotly
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import numpy as np
import time
import datetime
import psutil

plotly.tools.set_credentials_file(username='hapalop', api_key='k9minejjok', stream_ids=['yrxygxloge', '6dhsw2165g'])

print(tls.get_credentials_file())

stream_tokens = tls.get_credentials_file()['stream_ids']
print(stream_tokens)
token_1 = stream_tokens[-1]
token_2 = stream_tokens[-2]
print(token_1)
print(token_2)

stream_id1 = dict(token=token_1, maxpoints=60)
stream_id2 = dict(token=token_2, maxpoints=60)

trace1 = go.Scatter(x=[], y=[], stream=stream_id1, name='Sensor A', marker=dict(color='rgb(0,10,255)'))
trace2 = go.Scatter(x=[], y=[], stream=stream_id2, yaxis='y2', name='Sensor B', marker=dict(color='rgb(255,10,0)'))

data = [trace1, trace2]
layout = go.Layout(
    title='Streaming Sensor Data',
    legend=dict(
        x=1,
        y=100
    ),
    xaxis=dict(
        title='UTC (Coordinated Universal Time)',
    ),
    yaxis=dict(
        title='Chlorine Level (ppm) for Sensor A',
        rangemode='tozero',
        titlefont=dict(
            color='rgb(0,10,255)'
        ),
        tickfont=dict(
            color='rgb(0,10,255)'
        ),
    ),
    yaxis2=dict(
        title='Chlorine Level (ppm) for Sensor B',
        titlefont=dict(
            color='rgb(255,10,0)'
        ),
        tickfont=dict(
            color='rgb(255,10,0)'
        ),
        overlaying='y',
        side='right',
        rangemode='tozero',
    )
)

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='multple-trace-axes-streaming')

s_1 = py.Stream(stream_id=token_1)
s_2 = py.Stream(stream_id=token_2)

s_1.open()
s_2.open()

i = 0
while True:
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    delta = np.random.random()
    y1 = np.sin(i * 0.125 * np.pi) + 1 + np.random.random()
    y2 = np.cos(i * 0.125 * np.pi) + 2 + np.random.random()
    s_1.write(dict(x=x,y=y1))
    s_2.write(dict(x=x,y=y2))
    time.sleep(1)
    i += 1
s_1.close()
s_2.close()

tls.embed('streaming-demos','124')