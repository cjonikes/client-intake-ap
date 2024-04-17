"""
    Date created:   04/17/2024
    Date edited:    04/17/2024
    Sub-module:     server_logic.py
    Remarks:
"""

import json
import database.db_handler as database


def operation_selector(received_json_file):
    # Convert the received json file from client into a Python dict
    json_to_dict = json.dumps(received_json_file)

    # Retrieve the operation from the newly created dictionary
    operation = json_to_dict["operation"]
    results = None

    # Route the corresponding function to the requested operation.
    match operation:
        case "login":
            results = user_login_function(json_to_dict)
        case _:
            pass


    # Create the response JSON FILE
    dict_to_json = {
        "status": "COMPLETED",
        "data": results
    }

    # rebuild JSON FILE
    send_json_file = json.dumps(results, indent=4)

    # Return the results from the operation.
    return send_json_file


def user_login_function(json_to_dict):
    client_username = json_to_dict["data"]["username"]
    client_password = json_to_dict["data"]["passwd"]

    query = (f"SELECT * FROM user_login WHERE user_name = {client_username}"
             f"AND user_passwd = {client_password}")

    result = database.execute_query(query)

    response = {"response": False}
    if result:
        response["response"] = True

    return response


def two_function():
    pass
