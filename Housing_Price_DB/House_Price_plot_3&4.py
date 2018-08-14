''' the script is copyed and modified from a game revenue plot script, so the
varieties name will be weird'''

from plotly.offline import plot
import plotly.graph_objs as go
from pymongo import MongoClient
import pymongo

client = MongoClient()
DB = client.Housing_price
Collection = DB.Residence_level_3_and_4


#a function get the game name related data and return them as lists
def revenue_getter(game):    
    date = []
    revenue = []
    result = Collection.find({'city':game,'date':{'$exists':True}})
    result = result.sort('date', pymongo.ASCENDING)
    for item in result:
        date.append(item['date'])
        revenue.append(item['price'])
    return date,revenue,game


#prepare plot trace
def trace_getter(date,revenue,game):
    trace = go.Scatter(
        x = date,
        y = revenue,
        name = game)
    return trace

#prepare data list for plotting
def data_getter(trace,data):
    data.append(trace)
    return data

def main():
    data = []
    game_name = []
    game_name_temp = Collection.distinct('city')
    for name in game_name_temp:
        try:
            int(name)
        except ValueError:
            game_name.append(name)
    for g in game_name:
        date,revenue,game = revenue_getter(g)
        trace = trace_getter(date,revenue,game)
        data = data_getter(trace,data)
    data = data_getter(trace,data)
    plot(data,filename = 'level_3_and_4_cities.html')

if __name__ == "__main__":
    main()
        
