from pymongo import MongoClient
from bson import json_util
client = MongoClient()

db = client.crypto_data

def update(collection,filter,data):
        return db[collection].replace_one(filter, data,True)

def save(collection,data):
        print(f'data class:{data.__class__}')
        if isinstance(data,list):
                print('inserting list')
                db[collection].insert_many(data)
        else:
                print('inserting single entry')
                db[collection].insert_one(data)


def read(collection):
        return db[collection].find()

def read_one(collection,id):
        return db[collection].find_one({"id": id})