from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

class MessageController(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, required=True, location='json')
        args = parser.parse_args(strict=True)

        url = os.environ.get('MONGO_URL')
        client = MongoClient(url,connectTimeoutMS=30000,
                             socketTimeoutMS=None,
                             socketKeepAlive=True)
        db = client.get_default_database()
        # Test stuff
        result = db.messagestore.insert({"message" : args.message})
        print(result)
        return {"digest" : str(result)}

class MessagesController(Resource):

    def get(self, message_id):
        url = os.environ.get('MONGO_URL')
        client = MongoClient(url,connectTimeoutMS=30000,
                             socketTimeoutMS=None,
                             socketKeepAlive=True)
        db = client.get_default_database()
        # Test stuff
        result = db.messagestore.find_one({'_id': ObjectId(message_id)}, {'_id': False})
        print(result)
        return result
