from flask_sqlalchemy import SQLAlchemy
from factory.flask_setup import setup_api

def setup_db():
    app = setup_api()
    db = SQLAlchemy(app)
    return db