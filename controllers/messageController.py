from flask_restful import Resource, Api, reqparse
from bson.objectid import ObjectId
import os

class MessageController(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, required=True, location='json')
        args = parser.parse_args(strict=True)
        print(mongo)
        result = mongo.db.messagestore.insert({"message" : args.message})
        print(result)
        return {"digest" : str(result)}

class MessagesController(Resource):

    def get(self, message_id):
        print(mongo)
        result = mongo.db.messagestore.find_one({'_id': ObjectId(message_id)}, {'_id': False})
        return result
