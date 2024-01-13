"""
    Date created:   01/10/2024
    Date edited:    01/11/2024
    Sub-module:     access_point.py
    Remarks:        This submodule provides an access point singleton class to manage and establish
                    the connection with the server.
"""
import base64
import os
import socket
import time

import client.src.utilities.cryp_functions as encryptor
import Crypto.PublicKey.RSA as RSA

SERVER_IP = "192.168.56.1"
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

            cls._instance._gen_client_keys()

        return cls._instance

    # Client's private and public keys getters, and server public key getter
    def get_cprivate_key(self):
        return self._client_priv_key

    def get_cpublic_key(self):
        return self._client_pub_key

    def get_spublic_key(self):
        return self._server_pub_key

    # Key generator method
    def _gen_client_keys(self):
        self._instance._client_priv_key, self._instance._client_pub_key = encryptor.generate_key_pair()

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

    def handle_server(self):
        # This function is just a sequential execution block written in order to test
        # the server backend connection, key distribution and the transmission of a ciphertext

        # Establish a connection to the server.
        print("Establishing connection to the server")
        if self._instance._client_priv_key is None:
            print("true")
        self._instance._socket_conn = socket.socket()
        self._instance._socket_conn.connect((SERVER_IP, SERVER_PORT))

        # Send the following tag onto the open socket.
        client_msg = '!START'
        print("[CLIENT-REQUEST]:", client_msg)
        self._instance._socket_conn.send(client_msg.encode('utf-8'))

        # Await for the server response to continue.
        server_msg = self._instance._socket_conn.recv(2048)
        print("[SERVER-RESPONSE]:", server_msg)

        # Send the client public key from the current session to the server.
        key = self._instance._client_priv_key.public_key().public_bytes(
            encoding=encryptor.serialization.Encoding.PEM,
            format=encryptor.serialization.PublicFormat.SubjectPublicKeyInfo
        )
        self._instance._socket_conn.sendall(key)

        # Await for the server to provide a session public key back.
        server_msg = self._instance._socket_conn.recv(8192)
        self._instance._server_pub_key = encryptor.serialization.load_pem_public_key(server_msg,
                                                                                    backend=encryptor.default_backend())
        print("[SERVER-RESPONSE]:", server_msg)
        self._instance.set_spublic_key(server_msg)

        # Send tag to server to notify that the keys were received.
        client_msg = '!RECEIVED'
        print("[CLIENT-REQUEST]:", client_msg)
        self._instance._socket_conn.sendall(client_msg.encode('utf-8'))

        # Await for the server response for the previous tag.
        server_msg = self._instance._socket_conn.recv(8192)
        decoded_received = server_msg.decode('utf-8')
        print("[SERVER-RESPONSE]:", decoded_received)

        # Send tag to server to proceed with the next section of the code.
        client_msg = "!CONTINUE"
        encoded_send = client_msg.encode('utf-8')
        print("[CLIENT-REQUEST]:", client_msg)
        self._instance._socket_conn.send(encoded_send)

        # Await for the server to notify that the command was received.
        server_msg = self._instance._socket_conn.recv(8192)
        decoded_received = server_msg.decode('utf-8')
        print("[SERVER-RESPONSE]:", decoded_received)

        # Proceed on communicating using encryption
        # Send message to server
        toEncrypt = "hey there, this is the client"
        toEncode = encryptor.encrypt_msg(toEncrypt, self._instance._server_pub_key)
        self._instance._socket_conn.sendall(toEncode)

        # Await for the encrypted server response
        toReceive = self._instance._socket_conn.recv(8192)
        # toDecode = toReceive.decode('utf-8')
        toDecrypt = encryptor.decrypt_msg(toReceive, self._instance._client_priv_key)
        print("[SERVER-RESPONSE]:", toDecrypt)

        # Send the disconnect tag to the server
        client_msg = "!DISCONNECT"
        print("[CLIENT-REQUEST]:", client_msg)
        self._instance._socket_conn.sendall(client_msg.encode('utf-8'))

        # Await for the server response for the previous tag.
        server_msg = self._instance._socket_conn.recv(8192)
        decoded_received = server_msg.decode('utf-8')
        print("[SERVER-RESPONSE]:", decoded_received)


def get_access_point_instance():
    return access_point()
