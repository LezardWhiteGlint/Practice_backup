from plotly.offline import plot
import plotly.graph_objs as go
from pymongo import MongoClient
import pymongo

client = MongoClient()
DB = client.Mobile_revenue
Collection = DB.EZ_PZ_RPG_3D


#a function get the game name related data and return them as lists
def revenue_getter():    
    date = []
    revenue = []
    result = Collection.find({'date':{'$exists':True}})
    result = result.sort('date', pymongo.ASCENDING)
    for item in result:
        date.append(item['date'])
        revenue.append(item['revenue'])
    return date,revenue

#prepare plot trace
def trace_getter(date,revenue):
    trace = go.Scatter(
        x = date,
        y = revenue,
        name = 'EZ_PZ_RPG_3D')
    return trace

#prepare data list for plotting
def data_getter(trace,data):
    data.append(trace)
    return data

def main():
    data = []
    date,revenue = revenue_getter()
    trace = trace_getter(date,revenue)
    data = data_getter(trace,data)
    plot(data,filename = 'EZ_PZ_revenue.html')

if __name__ == "__main__":
    main()
        
