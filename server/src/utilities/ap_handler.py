"""
    Date created:   01/10/2023
    Date edited:    01/11/2023
    Sub-module:     ap_handler.py
    Remarks:        This submodule contains the access point handler blueprint to be used in threads when
                    a new connection to a client has been established.
"""

# Imports

import server.src.utilities.cryp_functions as encryptor
import asyncio


class client_handler:
    def __init__(self, conn, addr):
        self._server_priv_key = None
        self._server_pub_key = None
        self._client_pub_key = None
        self._client_socket = conn
        self._client_address = addr
        self._queue_manager_ref = None
        self.inputBuffer = None
        self.isAlive = True

        self._gen_server_keys()

        # Server's private and public keys getters, and client public key getter

    def get_sprivate_key(self):
        return self._server_priv_key

    def get_spublic_key(self):
        return self._server_pub_key

    def get_cpublic_key(self):
        return self._client_pub_key

    # Key generator method
    def _gen_server_keys(self):
        self._server_priv_key, self._server_pub_key = encryptor.generate_key_pair()

        # Server public Key setter

    def set_cpublic_key(self, client_key):
        self._client_pub_key = client_key

    async def open_connection(self):
        print("Connection open...")
        pass
        # Connection Logic
        # return a socket"

    def close_c_connection(self):
        pass
        # Close connection Logic

    def transmit_to_client(self, message):
        out_bound = encryptor.encrypt_msg(message, self.get_cpublic_key())

        # Socket Transmission Logic here

    def receive_from_client(self, inbound):
        message = encryptor.decrypt_msg(inbound, self.get_sprivate_key())
