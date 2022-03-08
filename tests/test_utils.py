from sqlite3 import Cursor
from db.seed_db import seed
import pytest
import psycopg2
from psycopg2 import Error
from db.connection import connect
from utils.utils import real_dict_user_conversion, load_json_file_data
from utils.classes import User

@pytest.fixture(autouse=True)
def run_around_tests():
    seed()

#test conversion to User class object from  (SELECT)
def test_utils_user_class():
    db = connect()
    cursor = db.cursor()
    query = '''SELECT * FROM users'''
    cursor.execute(query)
    users = cursor.fetchall()    
    user_list = real_dict_user_conversion(users)
    cursor.close()  
    db.close() 
    # loop through user objects and test contents
    assert len(user_list) == 8
    for user in user_list:
        assert user_list != 0
        assert isinstance(user, User) == True
        assert type(user.username) is str
        assert type(user.name) is str
        assert type(user.email) is str
        assert type(user.password) is str

    assert user_list[0].self_dict() == {
            "username": "pchatwin0",
            "name": "Parrnell Chatwin",
            "password": "wEShNQ2J2I",
            "email": "pchatwin0@blinklist.com"
    }

    assert user_list[-1].username == 'ebrickhill7'
    assert user_list[-1].name == 'Elysha Brickhill'
    assert user_list[-1].password == 'OyEF5HHEwCvn'
    assert user_list[-1].email == 'ebrickhill7@ft.com'

#test reading .JSON file to data
def test_json_file_read():
    data = load_json_file_data('db/data/user_data.json')
    assert type(data) == dict
    assert len(data["users"]) == 8
    assert data["users"][0] == {
            "username": "pchatwin0",
            "name": "Parrnell Chatwin",
            "password": "wEShNQ2J2I",
            "email": "pchatwin0@blinklist.com"
    }
