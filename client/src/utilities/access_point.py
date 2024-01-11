"""
    Date created:   01/10/2024
    Date edited:    01/11/2024
    Sub-module:     access_point.py
    Remarks:        This submodule provides an access point singleton class to manage and establish
                    the connection with the server.
"""

import client.src.utilities.cryp_functions as encryptor

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8000


class access_point:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(access_point, cls).__new__(cls)
            cls._instance._client_priv_key = None
            cls._instance._client_pub_key = None
            cls._instance._server_pub_key = None
            cls._instance._socket_conn = None
            cls._instance.isAlive = False
            cls._instance._inputBuffer = None

        return cls._instance

    # Client's private and public keys getters, and server public key getter
    def get_cprivate_key(self):
        return self.client_priv_key

    def get_cpublic_key(self):
        return self.client_pub_key

    def get_spublic_key(self):
        return self.server_pub_key

    # Key generator method
    def _gen_client_keys(self):
        self._instance.client_priv_key, self._instance.client_pub_key = encryptor.generate_key_pair()

    # Server public Key setter
    def set_spublic_key(self, server_key):
        self._instance.server_pub_key = server_key

    def open_connection(self):
        pass
        # Connection Logic
        # return a socket"

    def close_connection(self):
        pass
        # Close connection Logic

    def transmit_to_server(self, message):
        out_bound = encryptor.encrypt_msg(message, self._instance.get_spublic_key())

        # Socket Transmission Logic here

    def receive_from_server(self, inbound):
        message = encryptor.decrypt_msg(inbound, self._instance.get_cprivate_key())


def get_access_point_instance():
    return access_point()
