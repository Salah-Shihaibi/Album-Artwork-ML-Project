from connection import connect
import psycopg2
from psycopg2 import Error
from data.user_data import users

connection = connect()
def drop_table(table):
    try:     
        cursor = connection.cursor()
        #create new table
        drop_table_query = f'DROP TABLE IF EXISTS {table};'
        cursor.execute(drop_table_query)
        connection.commit()
        print(f"Table {table} dropped")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()


def create_user_table():
    try:     
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

def insert_users_data():
    try:
        cursor = connection.cursor()
        # Executing a SQL query to insert datetime into table
        insert_query = """ INSERT INTO users (username, name, password, email) VALUES (%(username)s, %(name)s, %(password)s, %(email)s)"""
        cursor.executemany(insert_query, users)
        connection.commit()
        print("users inserted successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            
def select_users_data():
    try:
        cursor = connection.cursor()
        # Executing a SQL query to insert datetime into table
        insert_query = """ SELECT * FROM users """
        cursor.execute(insert_query)
        x = cursor.fetchall()
        print(x)
        connection.commit()
        print("users retrieved successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()            
# for user in users:
#     insert_users_data(user)

drop_table("users")
create_user_table()
insert_users_data()
select_users_data()
