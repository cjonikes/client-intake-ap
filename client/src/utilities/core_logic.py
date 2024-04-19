"""
    Date created:   01/09/2024
    Date edited:    04/19/2024
    Sub-module:     core_logic.py
    Remarks:
"""

import sys
import json
import client.main as main
import client.src.frames.py.ui_logon as login_frame
import client.src.utilities.access_point as ap

from PySide6.QtWidgets import QApplication, QMainWindow

# Global Variables
MAIN_WINDOW = None
ACCESS_POINT = ap.get_access_point_instance()

APP_VERSION = f"{main.MAJOR_VERSION}.{main.MINOR_VERSION}.{main.PATCH_VERSION}"


class ui_logon(QMainWindow, login_frame.Ui_LoginWindow):
    """
        Remarks: Main window frame declaration and definition.
    """

    def __init__(self):
        """
            Remarks: Class definition
        """
        super().__init__()
        self.setupUi(self)

        # Update as version gets updated.
        self.setWindowTitle(f"APP_NAME - Ver. {APP_VERSION}")
        self.lblAppVersion.setText(str(APP_VERSION))

        # Store the username
        self.username = None

        # connect the buttons to the logic
        self.connect_signals_to_slots()

        # connect to the server
        try:
            ACCESS_POINT.open_connection()
        except Exception as e:
            print(f"[THREAD-ERROR] {str(e)}")

    def connect_signals_to_slots(self):
        self.btnSignIn.clicked.connect(self.get_credentials)
        self.btnClear.clicked.connect(self.clear_credentials)

    def get_credentials(self):
        self.username = self.leUsername.text()
        passwd = self.lePasswd.text()

        print(f"Username: {self.username}, password: {passwd}")

        data_to_send = {
            "username": self.username,
            "passwd": passwd
        }

        result = json_message_builder('w', "login", data_to_send)
        print(result)

        response = ACCESS_POINT.transmit_to_server(result)

    def clear_credentials(self):
        self.leUsername.clear()
        self.username = None
        self.lePasswd.clear()

        print("All containers have been cleared,")


def json_message_builder(operation_type, server_operation_type, data, received_json_file=None):
    """
    Remarks: builds a custom json file to be sent to the server.
    :param operation_type: character
    :type operation_type: char
    :param server_operation_type: string
    :type server_operation_type: str
    :param data: dictionary
    :type data: dict
    :param received_json_file: param for reading a json file.
    :return: JSON
    """

    result = None

    match operation_type:
        case 'r':
            result = json.load(received_json_file)
        case 'w':
            dict_to_json = {
                "operation": server_operation_type,
                "data": data
            }
            result = json.dumps(dict_to_json, indent=4)

    return result


def run_program():
    """
        Remarks: Handles the main execution of the program.
    """
    app = QApplication([])
    app.setStyle('Fusion')

    global MAIN_WINDOW
    MAIN_WINDOW = ui_logon()
    MAIN_WINDOW.show()

    sys.exit(app.exec())
