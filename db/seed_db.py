from factory.flask_setup import setup_api
from factory.db_setup import setup_db

app = setup_api()
db = setup_db()

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

