from flask import Flask
from flask_restful import Api
from controllers import helloController, messageController

app = Flask(__name__)
api = Api(app)

api.add_resource(helloController.HelloController, '/api/hello')
api.add_resource(messageController.MessageController, '/messages')
api.add_resource(messageController.MessagesController, '/messages/<message_id>')

if __name__ == '__main__':
    app.run(debug=True)
