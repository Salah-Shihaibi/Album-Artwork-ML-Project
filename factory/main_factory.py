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
    app.config.from_object(DevelopmentConfig()) 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    
    class User(db.Model):
        __tablename__='user'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __init__(self, id, username, email):
            self.id = id
            self.username = username
            self.email = email
            
    User.create()
    db.session.commit()
    api = Api(app)
     
    api.add_resource(Users, "/")
    api.add_resource(Psql, "/psql")
    return app

