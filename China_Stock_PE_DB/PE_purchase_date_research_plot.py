''' the script is copyed and modified from a game revenue plot script, so the
varieties name will be weird'''

from plotly.offline import plot
import plotly.graph_objs as go
from pymongo import MongoClient
import pymongo

client = MongoClient()
DB = client.China_stock
Collection = DB.Shanghai_stock


#a function get the game name related data and return them as lists
def revenue_getter(check):    
    date = []
    revenue = []
    result = Collection.find({'date':{'$exists':True}})
    result = result.sort('date', pymongo.ASCENDING)
    for item in result:
        if int(item['date'].split('-')[2]) == check:
            date.append(item['date'])
            revenue.append(item['average_PE'])
        else:
            continue
    return date,revenue


#prepare plot trace
def trace_getter(date,revenue,check):
    trace = go.Scatter(
        x = date,
        y = revenue,
        name = str(check))
    return trace

#prepare data list for plotting
def data_getter(trace,data):
    data.append(trace)
    return data

def main():
    data = []
    for i in range(31):
        check = i+1
        date,revenue = revenue_getter(check)
        trace = trace_getter(date,revenue,check)
        data = data_getter(trace,data)
    data = data_getter(trace,data)
    plot(data,filename = 'China_stock_shanghai_date_reserch.html')

if __name__ == "__main__":
    main()
        
