import pytest
from db.seed_db import seed
from db.connection import connect
import json 
db = connect()


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

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    response = client.post('/auth/register', data=json.dumps(user), headers=headers)
    assert response.status_code == 200
    assert response.json["user"] == user

def test_users_login(client):
    user = {
        "email":"pchatwin0@blinklist.com",
        "password":"wEShNQ2J2I"
    }
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    response = client.post('/auth/login', data=json.dumps(user), headers=headers)
    print("TESTLOG", response.json)
   
    assert response.status_code == 200
    assert response.json["user"] == user    
    
db.close()    
