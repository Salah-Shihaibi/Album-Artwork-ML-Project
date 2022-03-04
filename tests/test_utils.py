from sqlite3 import Cursor
from db.seed_db import seed
import pytest
import psycopg2
from psycopg2 import Error
from db.connection import connect
from utils.utils import real_dict_user_conversion
from utils.classes import User

@pytest.fixture(autouse=True)
def run_around_tests():
    seed()

#test conversion to User class object from  (SELECT)
def test_utils_user_class():
    try:
        db = connect()
        cursor = db.cursor()
        query = '''SELECT * FROM users'''
        cursor.execute(query)
        users = cursor.fetchall()    
        user_list = real_dict_user_conversion(users)
        cursor.close()  
        db.close() 
        # loop through user objects and test contents
        for user in user_list:
            assert user_list != 0
            assert isinstance(user, User) == True
            assert type(user.username) is str
            assert type(user.name) is str
            assert type(user.email) is str
            assert type(user.password) is str
    except:
        cursor.close()  
        db.close()  


  
