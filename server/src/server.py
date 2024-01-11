"""
    Date created:   01/10/2023
    Date edited:    01/11/2023
    Sub-module:     main.py
    Remarks:        Server program entry
"""
# Imports

import socket
import logging
import threading
from server.src.utilities import ap_handler


class server:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(server, cls).__new__(cls)
            cls._instance.connection_table = []
            cls._instance.connection_index = 0
            cls._instance.server_ip = socket.gethostbyname(socket.gethostname())
            cls._instance.server_port = 00000
            cls._instance.queue_manager_ref = None
            cls._instance.db_handler_ref = None

        return cls._instance

    def set_port(self, port):
        self._instance.server_port = port

    def run_server(self):
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.debug("Starting server...")
        print("[INFO]: Starting server...")
        print(f"[INFO]: Server IP: {self.server_ip}, Server Port: {self.server_port}")

        main_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        main_server.bind((self.server_ip, self.server_port))
        main_server.listen()

        print(f"[INFO]: Server is listening on {self.server_ip}:{self.server_port}")

        try:
            while True:
                print("[INFO]: Waiting for client...")
                conn, addr = main_server.accept()
                print(f"[INFO]: Client connected from: {addr}, socket: {conn}")
                t = threading.Thread(target=ap_handler.client_handler, args=(conn, addr))
                t.start()

                print(len(self.connection_table))
                self.connection_table.append(t)

        except KeyboardInterrupt:
            print("Server Stopped by Ctrl+C")
        finally:
            if main_server:
                main_server.close()
            for t in self.connection_table:
                t.join()

    def accept_connection(self):
        pass

    def show_active_conn(self):
        return self._instance.connection_table

    def _add_connection(self, ip, port, p_key):
        pass

    def _rm_connection(self, ip, port):
        pass


def get_server_instance():
    return server()