import psycopg2
from psycopg2 import Error
from db.connection import connect


def get_all_users():
    db = connect()
    cursor = db.cursor()
    query = """SELECT * FROM users"""
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    db.close()
    return users


def get_user_column(column, credential):
    db = connect()
    cursor = db.cursor()
    query = f"""SELECT * FROM users WHERE {column} = '{credential}' """
    cursor.execute(query)
    user = cursor.fetchall()
    cursor.close()
    db.close()
    return user
