import json
import pytest
from db.seed_db import seed
from utils.psql_utils import get_all_users
from utils.general_utils import headers


@pytest.fixture(autouse=True)
def run_around_tests():
    seed()


def test_users_register(client):
    user = {
        "username": "germanwhip2009",
        "name": "Jackson French",
        "email": "whippy95@hotmail.com",
        "password": "abcdefg",
    }
    # check if user can register
    response = client.post("/auth/register", data=json.dumps(user), headers=headers)
    assert response.status_code == 200
    assert response.json["user"] == user
    users = get_all_users()
    assert len(users) == 9


def test_email_in_use(client):
    user = {
        "username": "pchatwin0",
        "name": "Parrnell Chatwin",
        "password": "wEShNQ2J2I",
        "email": "pchatwin0@blinklist.com",
    }
    response = client.post("/auth/register", data=json.dumps(user), headers=headers)
    assert response.status_code == 400
    assert response.json["msg"] == "Email address is already in use."


def test_username_in_use(client):
    user = {
        "username": "pchatwin0",
        "name": "Parrnell Chatwin",
        "password": "wEShNQ2J2I",
        "email": "new_email@hotmail.com",
    }
    response = client.post("/auth/register", data=json.dumps(user), headers=headers)
    assert response.status_code == 400
    assert response.json["msg"] == "Username is already in use."


def test_invalid_email(client):
    invalid_email_user = {
        "username": "germanwhip2009",
        "name": "Jackson French",
        "email": "whippy95@h",
        "password": "abcdefgh",
    }
    response = client.post(
        "/auth/register", data=json.dumps(invalid_email_user), headers=headers
    )
    assert response.status_code == 400
    assert response.json["msg"] == "Email address invalid."


def test_invalid_password(client):
    short_password_user = {
        "username": "germanwhip2009",
        "name": "Jackson French",
        "email": "whippy95@hotmail.com",
        "password": "acc",
    }
    response = client.post(
        "/auth/register", data=json.dumps(short_password_user), headers=headers
    )
    assert response.status_code == 200
    assert response.json["msg"] == "Password should be 5 characters or longer."


def test_correct_body_error(client):
    user = {"password": "myPassWordIsWrong", "username": "pal", "name": "pal"}
    response = client.post("/auth/register", data=json.dumps(user), headers=headers)

    assert response.status_code == 400
    assert response.json["msg"] == "Credentials invalid format."


def test_correct_body_type_error(client):
    user = {
        "username": "OldMichaelGreogry",
        "name": None,
        "email": "whippy95@hotmail.com",
        "password": "cla1231nkerton",
    }
    response = client.post("/auth/register", data=json.dumps(user), headers=headers)

    assert response.status_code == 400
    assert response.json["msg"] == "Database ERROR: Data not provided."
