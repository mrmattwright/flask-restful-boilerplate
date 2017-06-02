from flask import Flask
from flask_restful import Api
from controllers import helloController, messageController
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api = Api(app)

#db = SQLAlchemy(app)

api.add_resource(helloController.HelloController, '/api/hello')
api.add_resource(messageController.MessageController, '/messages')

if __name__ == '__main__':
    app.run(debug=True)
