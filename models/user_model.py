from db.connection import connect
import psycopg2
from psycopg2 import Error


def register_user(user):
    try:
        db = connect()
        cursor = db.cursor()
        insert_query = """ INSERT INTO users (username, name, password, email) VALUES (%(username)s, %(name)s, %(password)s, %(email)s) RETURNING *"""
        cursor.execute(insert_query, user)
        user = cursor.fetchall()
        db.commit()
        cursor.close()
        db.close()
        return user[0]
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        cursor.close()
        db.close()


def login_user(cred):
    try:
        db = connect()
        cursor = db.cursor()
        insert_query = """SELECT * FROM users WHERE email = %s"""
        cursor.execute(insert_query, (cred['email'],))
        user = cursor.fetchall()
        if cred['password'] == user[0]['password']:
            print('error incorrect password')
        db.commit()
        cursor.close()
        db.close()
        return user[0]
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        cursor.close()
        db.close()