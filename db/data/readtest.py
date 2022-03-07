import os
import json


def read_test():
    with open (os.path.join("db/data", 'user_data.json')) as json_file:
        data = json.load(json_file)
        # users = data[users]
        print(data["users"][0]["name"])
        for letter in data["users"][0]["name"]:
            print(letter)


read_test()