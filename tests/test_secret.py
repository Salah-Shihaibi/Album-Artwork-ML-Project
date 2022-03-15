from flask import json
from firebase_app import auth
from utils.general_utils import sign_in_test_user

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

    response = sign_in_test_user(user)

    headers = {"authorization": response["idToken"]}
    response = client.get("/secret", headers=headers)
    assert response.json["secret"] == "I have an identical twin, also called ed"
    assert response.status_code == 200


# invalid token returns status code 401, and appropriate error message
def test_jwt_invalid_code(client):

    users = auth.list_users()

    for user in users.users:
        auth.delete_user(user.uid)

    # create new user
    user = auth.create_user(
        email="firstUser@user.com",
        password="password123",
    )

    response = sign_in_test_user(user)

    headers = {"authorization": ""}
    response = client.get("/secret", headers=headers)
    assert (
        response.json["msg"]
        == "Illegal ID token provided: b''. ID token must be a non-empty string."
    )
    assert response.status_code == 401


# invalid token returns status code 401, and appropriate error message
def test_jwt_invalid_code_2(client):

    users = auth.list_users()

    for user in users.users:
        auth.delete_user(user.uid)

    # create new user
    user = auth.create_user(
        email="firstUser@user.com",
        password="password123",
    )

    response = sign_in_test_user(user)

    headers = {"authorization": "wrong"}
    response = client.get("/secret", headers=headers)
    assert response.json["msg"] == "Wrong number of segments in token: b'wrong'"
    assert response.status_code == 401


# invalid user returns 401, and not granted access
def test_jwt_super_secret_invalid(client):

    users = auth.list_users()

    for user in users.users:
        auth.delete_user(user.uid)

    # create new user
    user = auth.create_user(
        email="firstUser@user.com",
        password="password123",
    )

    auth.set_custom_user_claims(user.uid, {"admin": False})

    response = sign_in_test_user(user)

    headers = {"authorization": response["idToken"]}
    response = client.get("/superSecret", headers=headers)
    assert response.json["access"] == "NOT granted"
    assert response.status_code == 401


# valid token returns status code 200, and admin access
def test_jwt_super_secret(client):

    users = auth.list_users()

    for user in users.users:
        auth.delete_user(user.uid)

    # create new user
    user = auth.create_user(
        email="firstUser@user.com",
        password="password123",
    )

    auth.set_custom_user_claims(user.uid, {"admin": True})

    response = sign_in_test_user(user)

    headers = {"authorization": response["idToken"]}
    response = client.get("/superSecret", headers=headers)
    assert response.json["access"] == "granted"
    assert response.status_code == 200


# valid token returns status code 200, and admin access
def test_jwt_manage_user_access(client):

    users = auth.list_users()

    for user in users.users:
        auth.delete_user(user.uid)

    # create new users
    user2 = auth.create_user(
        email="secondUser@user.com",
        password="password123",
    )
    auth.set_custom_user_claims(user2.uid, {"admin": False})

    user = auth.create_user(
        email="firstUser@user.com",
        password="password123",
    )
    auth.set_custom_user_claims(user.uid, {"admin": True})

    response = sign_in_test_user(user)

    headers = {
        "authorization": response["idToken"],
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = client.patch(
        "/manage_user_access",
        data=json.dumps({"uid": user2.uid, "admin": "true"}),
        headers=headers,
    )

    test_user = auth.get_user(user2.uid)

    assert response.status_code == 204
    assert test_user.custom_claims["admin"] == "true"
