import pytest
from db.seed_db import seed
from utils.general_utils import real_dict_user_conversion, load_json_file_data
from utils.classes import User
from utils.psql_utils import get_all_users


@pytest.fixture(autouse=True)
def run_around_tests():
    seed()


# test conversion to User class object from  (SELECT)
def test_utils_user_class():
    users = get_all_users()
    user_list = real_dict_user_conversion(users)
    # loop through user objects and test contents
    assert len(user_list) == 8
    for user in user_list:
        assert user_list != 0
        assert isinstance(user, User)
        assert isinstance(user.username, str)
        assert isinstance(user.name, str)
        assert isinstance(user.email, str)
        assert isinstance(user.password, str)

    assert user_list[0].self_dict() == {
        "username": "pchatwin0",
        "name": "Parrnell Chatwin",
        "password": "wEShNQ2J2I",
        "email": "pchatwin0@blinklist.com",
    }

    assert user_list[-1].username == "ebrickhill7"
    assert user_list[-1].name == "Elysha Brickhill"
    assert user_list[-1].password == "OyEF5HHEwCvn"
    assert user_list[-1].email == "ebrickhill7@ft.com"


# test reading .JSON file to data
def test_json_file_read():
    data = load_json_file_data("db/data/user_data.json")
    assert isinstance(data, dict)
    assert len(data["users"]) == 8
    assert data["users"][0] == {
        "username": "pchatwin0",
        "name": "Parrnell Chatwin",
        "password": "wEShNQ2J2I",
        "email": "pchatwin0@blinklist.com",
    }
