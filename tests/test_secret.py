from flask import request
from firebase_app import auth
import requests

# no JWT sent
def test_no_jwt_sent(client):
    headers = {}
    response = client.get("/secret", headers=headers)
    assert response.status_code == 401
    headers = {"authorization": ""}
    response = client.get("/secret", headers=headers)
    assert response.status_code == 401


# valid token returns status code 200, and ed's secret
def test_jwt_valid_code(client):

    users = auth.list_users()

    for user in users.users:
        auth.delete_user(user.uid)

    # create new user
    user = auth.create_user(
        email="firstUser@user.com",
        password="password123",
    )

    response = sign_in_test_user()
    print(response)

    headers = {"authorization": response["idToken"]}
    response = client.get("/secret", headers=headers)
    assert response.json["secret"] == "I have an identical twin, also called ed"
    assert response.status_code == 200


sign_in_url = "http://localhost:9099/identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=fake-key"


def sign_in_test_user():
    response = requests.post(
        sign_in_url, json={"email": "firstUser@user.com", "password": "password123"}
    )
    return response.json()


# invalid token returns status code 401, and appropriate error message
def test_jwt_valid_code(client):

    users = auth.list_users()

    for user in users.users:
        auth.delete_user(user.uid)

    # create new user
    user = auth.create_user(
        email="firstUser@user.com",
        password="password123",
    )

    response = sign_in_test_user()
    print(response)

    headers = {"authorization": ""}
    response = client.get("/secret", headers=headers)
    assert (
        response.json["msg"]
        == "Illegal ID token provided: b''. ID token must be a non-empty string."
    )
    assert response.status_code == 401


# invalid token returns status code 401, and appropriate error message
def test_jwt_valid_code(client):

    users = auth.list_users()

    for user in users.users:
        auth.delete_user(user.uid)

    # create new user
    user = auth.create_user(
        email="firstUser@user.com",
        password="password123",
    )

    response = sign_in_test_user()
    print(response)

    headers = {"authorization": "wrong"}
    response = client.get("/secret", headers=headers)
    assert response.json["msg"] == "Wrong number of segments in token: b'wrong'"
    assert response.status_code == 401
