from flask import Flask
from flask_restful import Api
from controllers.user_controller import Register, Admin_users, Login
from config import DevelopmentConfig
# from flask_sqlalchemy import SQLAlchemy
from factory.flask_setup import setup_api
from factory.db_setup import setup_db
#from db.seed_db import User


def create_app():
    # app = setup_api()
    # db = setup_db()
    app = Flask(__name__)
    api = Api(app)
     
    api.add_resource(Register, "/auth/register")
    api.add_resource(Login, "/auth/login")
    api.add_resource(Admin_users, "/admin")

    return app


