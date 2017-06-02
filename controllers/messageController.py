from flask_restful import Resource

class MessageController(Resource):

    def get(self):
        return {"response" : "messages get"}

    def post(self):
        return {"response" : "messages post"}
