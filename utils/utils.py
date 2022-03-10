from utils.classes import User
import json


def real_dict_user_conversion(real_dict_list):
    # create empty user list
    user_list = []
    # loop through user tuples and convert into user objects
    for user in real_dict_list:

        newUser = User(user["username"], user["name"], user["password"], user["email"])
        user_list.append(newUser)

    return user_list


def load_json_file_data(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data

