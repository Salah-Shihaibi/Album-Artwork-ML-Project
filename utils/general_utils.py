import json
import requests
from utils.classes import User


def real_dict_user_conversion(real_dict_list):
    # create empty user list
    user_list = []
    # loop through user tuples and convert into user objects
    for user in real_dict_list:

        newUser = User(user["username"], user["name"], user["password"], user["email"])
        user_list.append(newUser)

    return user_list


def load_json_file_data(file_path):
    with open(file_path, encoding="ascii") as json_file:
        data = json.load(json_file)
        return data


headers = {"Content-Type": "application/json", "Accept": "application/json"}


def sign_in_test_user(user):
    sign_in_url = "http://localhost:9099/identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=fake-key"
    response = requests.post(
        sign_in_url,
        json={"email": user.email, "password": "password123"},
    )
    return response.json()
