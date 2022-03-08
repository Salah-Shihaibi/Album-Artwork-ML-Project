from flask import Flask
from flask_restful import Api
from controllers.user_controller import Register, Login, Ping
from config import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Ping, "/")
    api.add_resource(Register, "/auth/register")
    api.add_resource(Login, "/auth/login")

    return app
