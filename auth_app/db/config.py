# from auth_app import app
# from flask_pymongo import PyMongo
# import mongoengine
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'your_database_name',
#     'host': 'your_mongodb_uri',  
# }
# #mongoengine.connect(host="mongodb://127.0.0.1:27017/mongoEngine")
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/API_Hits'
# mongo = PyMongo(app)
from mongoengine import connect

def connect_to_db():
    db_name = 'mongoEngine'
    db_host = 'mongodb://localhost:27017/mongoEngine'
    connect(db=db_name, host=db_host)