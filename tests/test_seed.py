from db.seed_db import seed
import pytest
import psycopg2
from psycopg2 import Error
from db.connection import connect

db = connect()

@pytest.fixture(autouse=True)
def run_around_tests():
    seed()

   
#test tables exist
def test_db_tables():
    cursor = db.cursor()
    query = """
            SELECT EXISTS(SELECT 1 FROM information_schema.tables 
            WHERE table_catalog='album_cover_db' AND 
                    table_schema='public' AND 
                    table_name='users'); 
                    """
    cursor.execute(query)
    x = cursor.fetchone()
    assert x["exists"] == True
   
#test data in tables (SELECT)
def test_tables_users():
    cur = db.cursor()
    query = '''SELECT * FROM users'''
    cur.execute(query)
    users = cur.fetchall()
    assert len(users) == 8
  
