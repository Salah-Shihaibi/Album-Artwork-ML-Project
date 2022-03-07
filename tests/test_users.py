import pytest
from db.seed_db import seed
from db.connection import connect
import json
from utils.psql_utils import get_all_users


@pytest.fixture(autouse=True)
def run_around_tests():
    seed()

mimetype = 'application/json'
headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }









def test_users_login(client):
    user = {
        "password": "wEShNQ2J2I",
        "email": "pchatwin0@blinklist.com"
    }
    user_return = {"username": "pchatwin0",
                   "name": "Parrnell Chatwin",
                   "password": "wEShNQ2J2I",
                   "email": "pchatwin0@blinklist.com"}

    response = client.post(
        '/auth/login', data=json.dumps(user), headers=headers)

    assert response.status_code == 200
    assert response.json["user"] == user_return


    


