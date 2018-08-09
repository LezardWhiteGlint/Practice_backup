from plotly.offline import plot
import plotly.graph_objs as go
from pymongo import MongoClient
import pymongo

client = MongoClient()
DB = client.Mobile_revenue
Collection = DB.revenue


#a function get the game name related data and return them as lists
def revenue_getter(game):    
    date = []
    revenue = []
    result = Collection.find({'game':game,'date':{'$exists':True}})
    result = result.sort('date', pymongo.ASCENDING)
    for item in result:
        date.append(item['date'])
        revenue.append(item['revenue'])
    return date,revenue,game

def total_revenue_getter():
    date = []
    revenue = []
    pipeline = [{'$group':{'_id':{'date':'$date'},'revenue':{'$sum':'$revenue'}}},
                {'$sort':{'_id':1}}]
    result = Collection.aggregate(pipeline)
    for item in result:
        date.append(item['_id']['date'])
        revenue.append(item['revenue'])
    return date,revenue,'Total Revenue'
    

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
    game_name_temp = Collection.distinct('game')
    for name in game_name_temp:
        try:
            int(name)
        except ValueError:
            game_name.append(name)
    for g in game_name:
        date,revenue,game = revenue_getter(g)
        trace = trace_getter(date,revenue,game)
        data = data_getter(trace,data)
    date,revenue,game = total_revenue_getter()
    trace = trace_getter(date,revenue,game)
    data = data_getter(trace,data)
    plot(data,filename = 'Mobile_Games_revenue.html')

if __name__ == "__main__":
    main()
        
