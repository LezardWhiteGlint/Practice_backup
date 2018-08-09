from pymongo import MongoClient
client = MongoClient()

DB = client.Mobile_revenue
revenue = DB.revenue

