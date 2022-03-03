from flask_restful import Resource
import psycopg2
from psycopg2 import Error
from flask import jsonify, make_response, abort


def create_tables():
    try:
        connection = psycopg2.connect(user = "postgres",
                                    password="0000",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="album_cover_db"
                                    )
        cursor = connection.cursor()
        #create new table
        create_table_query = """
        CREATE TABLE users (
          username VARCHAR(50) PRIMARY KEY,
          name VARCHAR(50) NOT NULL,
          email VARCHAR(100) UNIQUE,
          password VARCHAR(100) NOT NULL
          );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PSQL")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

class Users(Resource):
        def get(self):
            return 200


class Psql(Resource):
        def get(self):
            create_tables()
            return 200


class Admin_users(Resource):
    def get(self):        
        return make_response(jsonify({'body': 'You are an admin'}), 200)
