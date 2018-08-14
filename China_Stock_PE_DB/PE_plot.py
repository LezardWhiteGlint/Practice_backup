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
def revenue_getter(game):    
    date = []
    revenue = []
    result = Collection.find({'date':{'$exists':True}})
    result = result.sort('date', pymongo.ASCENDING)
    for item in result:
        date.append(item['date'])
        revenue.append(item[game])
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
    game_name_temp = ['total_stock_value(100M_RMB)',
                      'trading_value(100M_RMB)',
                      'trade_volum(10K_Unit)',
                      'trade_amount(100M_RMB)',
                      'traded_times(10K_times)',
                      'average_PE',
                      'exchange_rate']
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
    plot(data,filename = 'China_stock_shanghai.html')

if __name__ == "__main__":
    main()
        
