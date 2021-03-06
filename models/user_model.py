from psycopg2 import Error
from db.connection import connect
from error_handling.error_classes import (
    NoUserFoundError,
    IncorrectPasswordError,
    SQLErrorHandler,
)


def register_user(user):
    try:
        db = connect()
        cursor = db.cursor()
        insert_query = """INSERT INTO users
        (username, name, password, email) VALUES
        (%(username)s, %(name)s, %(password)s, %(email)s)
        RETURNING *"""
        cursor.execute(insert_query, user)
        user = cursor.fetchall()
        db.commit()
        cursor.close()
        db.close()
        return user[0]
    except Error as error:
        cursor.close()
        db.close()
        raise SQLErrorHandler(error.pgcode) from error
    except Exception as error:
        cursor.close()
        db.close()
        raise error


def login_user(cred):

    try:
        db = connect()
        cursor = db.cursor()
        insert_query = """SELECT * FROM users WHERE email = %s"""
        cursor.execute(insert_query, (cred["email"],))
        user = cursor.fetchall()
        if len(user) == 0:
            raise NoUserFoundError
        if cred["password"] != user[0]["password"]:
            raise IncorrectPasswordError
        db.commit()
        cursor.close()
        db.close()
        return user[0]
    except Error as error:
        cursor.close()
        db.close()
        raise SQLErrorHandler(error.pgcode) from error
    except Exception as error:
        db.close()
        raise error
