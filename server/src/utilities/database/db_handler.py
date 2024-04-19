"""
    Date created:   04/17/2024
    Date edited:    04/19/2024
    Sub-module:     db_handler.py
    Remarks:        this sub-module controls the query executions from the client to the database.
"""

import psycopg2
from server.src.utilities.database.config import load_config


def set_connection():
    config = load_config()
    database_connection = connect(config)
    return database_connection


def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('[SERVER-INFO] Connected to the PostgreSQL database.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def read_from_database(database_connection):
    # cursor = None
    try:
        # Retrieve values from the database.
        cursor = database_connection.cursor()
        sql_command = "select * from user_login"

        cursor.execute(sql_command)
        user_login_records = cursor.fetchall()

        for row in user_login_records:
            print("ID = ", row[0], )
            print("userName = ", row[1], )
            print("Password = ", row[2], "\n")

    except(Exception, psycopg2.Error) as Error:
        print("Error while fetching data from PostgreSQL")

    finally:
        if database_connection:
            cursor.close()


def execute_query(sql_query, database_connection):
    retrieved_results = None

    try:
        # Retrieve values from the database.
        cursor = database_connection.cursor()
        cursor.execute(sql_query)
        retrieved_results = cursor.fetchall()

        return retrieved_results

    except(Exception, psycopg2.Error) as Error:
        print(f"Error while executing the query {sql_query}. Error = {Error}")

    finally:
        if database_connection:
            cursor.close()

# if __name__ == '__main__':
#     config = load_config()
#     DATABASE_CONNECTION = connect(config)
#     read_from_database()
