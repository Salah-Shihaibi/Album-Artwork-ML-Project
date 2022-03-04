from db.connection import connect
import psycopg2
from psycopg2 import Error
db = connect()

def register_user(user):
    try:
        cursor = db.cursor()
        insert_query = """ INSERT INTO users (username, name, password, email) VALUES (%(username)s, %(name)s, %(password)s, %(email)s) RETURNING *"""
        cursor.execute(insert_query, user)
        user = cursor.fetchall()
        db.commit()
        print(user)
        print("users inserted successfully")
        cursor.close()
        return user[0]
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        cursor.close()


def login_user(cred):
    try:
        print(cred)
        cursor = db.cursor()
        print(cred['email'])
        insert_query = """SELECT * FROM users WHERE email = %s"""
        cursor.execute(insert_query, cred['email'])
        user = cursor.fetchall()
        print(cred['password'], user['password'], 'Module')
        db.commit()
        print("users logged in successfully")
        cursor.close()
        return user[0]
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        cursor.close()

