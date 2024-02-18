from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.everyaitools

collection = db.Url

new_collection = db.UpdatedUrl
