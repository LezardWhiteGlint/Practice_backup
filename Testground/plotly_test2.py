import plotly.graph_objs as go
import plotly.plotly as py

trace = {'x':['2018-1-1','2018-1-2','2018-1-3','2018-1-4','2018-1-5','2018-1-6','2018-1-7'],'y':[1,2,3,4,5,6,7]}
data = [trace]
layout ={}
fig = go.Figure(data = data, layout = layout)

plot_url = py.plot(fig)
