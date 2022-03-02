from flask import Flask
from flask_restful import Api
from controllers.user_controller import Users, Psql
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy

def create_app():
    print(app.config.from_envvar("DATABASE_URI"))
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig()) 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config.from_envvar("DATABASE_URI")
    db = SQLAlchemy(app)
    api = Api(app)

    api.add_resource(Users, "/")
    api.add_resource(Psql, "/psql")
    return app




