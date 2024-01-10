"""
    Date created:   01/09/2024
    Date edited:    01/09/2024
    Sub-module:     core_logic.py
    Remarks:
"""

import sys
import client.main as main
import client.src.frames.py.ui_logon as lg

from PySide6.QtWidgets import QApplication, QMainWindow

# Global Variables
MAIN_WINDOW = None


APP_VERSION = f"{main.MAJOR_VERSION}.{main.MINOR_VERSION}.{main.PATCH_VERSION}"


class ui_main(QMainWindow, lg.Ui_LoginWindow):
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


def run_program():
    """
        Remarks: Handles the main execution of the program.
    """
    app = QApplication([])
    app.setStyle('Fusion')

    global MAIN_WINDOW
    MAIN_WINDOW = ui_main()
    MAIN_WINDOW.show()

    sys.exit(app.exec())
