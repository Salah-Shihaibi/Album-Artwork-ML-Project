import pytest
from db.seed_db import seed
from db.connection import connect


@pytest.fixture(autouse=True)
def run_around_tests():
    seed()


# test tables exist
def test_db_tables():

    db = connect()
    cursor = db.cursor()
    query = """
            SELECT EXISTS(SELECT 1 FROM information_schema.tables 
            WHERE table_catalog='album_cover_db' AND 
                    table_schema='public' AND 
                    table_name='users'); 
                    """
    cursor.execute(query)
    x = cursor.fetchone()
    cursor.close()
    db.close()
    assert x["exists"] == True


# test data in tables (SELECT)
def test_tables_users():
    db = connect()
    cursor = db.cursor()
    query = """SELECT * FROM users"""
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    db.close()
    assert len(users) == 8
