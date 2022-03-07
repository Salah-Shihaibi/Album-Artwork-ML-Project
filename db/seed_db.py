from db.connection import connect
import psycopg2
from psycopg2 import Error
# from db.data.user_data import users
from utils.utils import load_json_file_data



def drop_table(table):
    try:
        db = connect()     
        cursor = db.cursor()
        #create new table
        drop_table_query = f'DROP TABLE IF EXISTS {table};'
        cursor.execute(drop_table_query)
        db.commit()
        print(f"Table {table} dropped")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if db:
            cursor.close()
            db.close()

def create_user_table():
    try:
        db = connect()     
        cursor = db.cursor()
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
        db.commit()
        print("Table created successfully in PSQL")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if db:
            cursor.close()
            db.close()

def insert_users_data():
    try:
        db = connect()
        cursor = db.cursor()
        # Executing a SQL query to insert datetime into table
        insert_query = """ INSERT INTO users (username, name, password, email) VALUES (%(username)s, %(name)s, %(password)s, %(email)s)"""
       
        data = load_json_file_data('db/data/user_data.json')
        users = data["users"]
              
        cursor.executemany(insert_query, users)
        db.commit()
        print("users inserted successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if db:
            cursor.close()
            db.close()                  

def seed():
    drop_table("users")
    create_user_table()
    insert_users_data()



