from flask import Flask
from config import DevelopmentConfig

def setup_api():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig()) 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app