"""
    Date created:   01/10/2024
    Date edited:    01/10/2024
    Sub-module:     verification.py
    Remarks:        this module is used for validation and verification of different types of inputs
"""
import re


def input_checker(type, input):
    """
        Remarks: This function validate different inputs types
    """
    is_valid = True
    # Check length
    if type == "username":
        if len(input) < 3 or len(input) > 30:
            is_valid = False

        # Check allowed characters (alphanumeric and underscore)
        if not re.match("^[a-zA-Z0-9_]+$", input):
            is_valid = False

    # elif type == "passwords":
    #     pass

    # All checks passed, username is valid
    return is_valid


# Example usage:
username_to_check = "new_user123"
if input_checker("username", username_to_check):
    print(f"The username '{username_to_check}' is valid.")
else:
    print(f"The username '{username_to_check}' is not valid.")
