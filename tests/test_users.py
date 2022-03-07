import pytest
from db.seed_db import seed
from db.connection import connect
import json 

@pytest.fixture(autouse=True)
def run_around_tests():
    seed()

def test_users_register(client):
    user = {
        "username":"germanwhip2009",
        "name":"Jackson French",
        "email":"whippy95@hotmail.com",
        "password":"abcdefg"
    }

    short_password_user =  {
        "username":"germanwhip2009",
        "name":"Jackson French",
        "email":"whippy95@hotmail.com",
        "password":"abcg"
    }

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    # check if user can register
    response = client.post('/auth/register', data=json.dumps(user), headers=headers)
    assert response.status_code == 200
    assert response.json["user"] == user

    # check if password is too short
    response = client.post('/auth/register', data=json.dumps(short_password_user), headers=headers)
    assert response.status_code == 400
    assert response.json["msg"] == 'incorrect password' 


    db = connect()
    cursor = db.cursor()
    query = '''SELECT * FROM users'''
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    db.close()
    assert len(users) == 9

def test_users_login(client):
    user = {
    "password": "wEShNQ2J2I",
    "email": "pchatwin0@blinklist.com"
    }
    user_return = {"username": "pchatwin0",
                    "name": "Parrnell Chatwin",
                    "password": "wEShNQ2J2I",
                    "email": "pchatwin0@blinklist.com"}
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    response = client.post('/auth/login', data=json.dumps(user), headers=headers)
   
    assert response.status_code == 200
    assert response.json["user"] == user_return 
    
