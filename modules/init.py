from pymongo import MongoClient

import os

def init_mongo_client():
    URI = os.getenv('MONGO_URI')

    if not URI or URI == '':
        raise ValueError('Wrong Mongo URI provided!')

    client = MongoClient(URI)

    # Test connection 
    try:
        client_info = client.server_info()
    except:
        raise RuntimeError('Could not init Mongo')

    return client['ai']

def init_modules():
    return {
       'mongo': init_mongo_client()
    }