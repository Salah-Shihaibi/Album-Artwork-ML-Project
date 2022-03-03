from flask import Flask
from flask_restful import Api
from controllers.user_controller import Users, Psql
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from factory.flask_setup import setup_api
from factory.db_setup import setup_db
#from db.seed_db import User


def create_app():
    # app = setup_api()
    # db = setup_db()
    app = Flask(__name__)
    api = Api(app)
     
    api.add_resource(Users, "/")
    api.add_resource(Psql, "/psql")
    return app


