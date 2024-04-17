"""
    Date created:   04/17/2024
    Date edited:    04/17/2024
    Sub-module:
    Remarks:
"""

import psycopg2
from config import load_config

DATABASE_CONNECTION = None
def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def read_from_database():
    try:
        # Retrieve values from the database.
        cursor = DATABASE_CONNECTION.cursor()
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
        if DATABASE_CONNECTION:
            cursor.close()


def execute_query(sql_query):

    retrieved_results = None
    cursor = None

    try:
        if sql_query:
            # Retrieve values from the database.
            cursor = DATABASE_CONNECTION.cursor()

            cursor.execute(sql_query)
            retrieved_results = cursor.fetchall()

        return retrieved_results

    except(Exception, psycopg2.Error) as Error:
        print(f"Error while executing the query {sql_query}. Error = {Error}")

    finally:
        if DATABASE_CONNECTION:
            cursor.close()


if __name__ == '__main__':
    config = load_config()
    DATABASE_CONNECTION = connect(config)
    read_from_database()

