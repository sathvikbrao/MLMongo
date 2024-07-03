with open('model.joblib','rb') as file:
    model_bytes = file.read()

import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['modeldb'] #use modeldb /database
collection = db['models'] # db.models Here models is collections

collection.insert_one({'model_name': 'random_forest', 'model': model_bytes})