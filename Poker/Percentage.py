from pymongo import MongoClient
import pymongo
from collections import defaultdict
from plotly.offline import plot
import plotly.graph_objs as go
import ast

player_num = 7

client = MongoClient()
DB = client.Poker
Collection = DB['player_num_'+str(player_num)]



results_all = Collection.find({'tag':'all'})
results_winner = Collection.find({'tag':'winner'})


def process_data(results):
    stat = defaultdict(int)
    for r in results:
        key = []
        key_temp = r['initial_hand']
        # using ast to convert the string into list
        try:
            key_temp = ast.literal_eval(key_temp)
        except ValueError:
            pass
        for i in key_temp:
            key.append(i[1])
        key.sort()
        for c in range(2):
            if key[c] == 11:
                key[c] = 'J'
            if key[c] == 12:
                key[c] = 'Q'
            if key[c] == 13:
                key[c] = 'K'
            if key[c] == 14:
                key[c] = 'A'
        stat[str(key)] += 1
    return stat


total = process_data(results_all)
winner = process_data(results_winner)

x_bar = []
y_bar = []



k_temp = []
for i in winner:
	k_temp.append(i)
k_temp.sort()
#print(total)
for i in k_temp:
    #x_bar.append(i)
    y_bar.append(winner[i]/total[i])
y_bar.sort()
for i in range(len(y_bar)):
    if 
    #print(y_bar)

data = [go.Bar(
    x = x_bar,
    y = y_bar)]

plot(data,filename = 'Poker.html')
