from flask import Flask
from flask_restful import Api
from controllers.user_controller import Users

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Users, "/")

    return app




