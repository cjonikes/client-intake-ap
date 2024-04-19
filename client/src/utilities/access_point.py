"""
    Date created:   01/10/2024
    Date edited:    04/19/2024
    Sub-module:     access_point.py
    Remarks:        This submodule provides an access point singleton class to manage and establish
                    the connection with the server.
"""

import socket
import client.src.utilities.cryp_functions as encryptor

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 8000


class access_point:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(access_point, cls).__new__(cls)
            cls._instance._client_private_key = None
            cls._instance._client_public_key = None
            cls._instance._server_public_key = None
            cls._instance._socket_connection = None
            cls._instance.is_alive = False
            cls._instance._input_buffer = None

            cls._instance._generate_client_keys()

        return cls._instance

    # Client's private and public keys getters, and server public key getter
    def get_client_private_key(self):
        return self._client_private_key

    def get_client_public_key(self):
        return self._client_public_key

    def get_server_public_key(self):
        return self._server_public_key

    # Key generator method
    def _generate_client_keys(self):
        self._instance._client_private_key, self._instance._client_public_key = encryptor.generate_key_pair()

    # Server public Key setter
    def set_server_public_key(self, server_key):
        self._instance.server_pub_key = server_key

    def open_connection(self):
        # Establish a connection to the server.
        print("Establishing connection to the server")
        if self._instance._client_private_key is None:
            print("true")
        self._instance._socket_connection = socket.socket()
        self._instance._socket_connection.connect((SERVER_IP, SERVER_PORT))

        # Send the following tag onto the open socket.
        client_msg = '!START'
        print("[CLIENT-REQUEST]:", client_msg)
        self._instance._socket_connection.send(client_msg.encode('utf-8'))

        # Await for the server response to continue.
        server_msg = self._instance._socket_connection.recv(2048)
        print("[SERVER-RESPONSE]:", server_msg)

        # Send the client public key from the current session to the server.
        key = self._instance._client_private_key.public_key().public_bytes(
            encoding=encryptor.serialization.Encoding.PEM,
            format=encryptor.serialization.PublicFormat.SubjectPublicKeyInfo
        )
        self._instance._socket_connection.sendall(key)

        # Await for the server to provide a session public key back.
        server_msg = self._instance._socket_connection.recv(8192)
        self._instance._server_public_key = encryptor.serialization.load_pem_public_key(server_msg,
                                                                                     backend=encryptor.default_backend())
        print("[SERVER-RESPONSE]:", server_msg)
        # self._instance.set_server_public_key(server_msg)

        # Send tag to server to notify that the keys were received.
        client_msg = '!RECEIVED'
        print("[CLIENT-REQUEST]:", client_msg)
        self._instance._socket_connection.sendall(client_msg.encode('utf-8'))

        # Await for the server response for the previous tag.
        server_msg = self._instance._socket_connection.recv(8192)
        decoded_received = server_msg.decode('utf-8')
        print("[SERVER-RESPONSE]:", decoded_received)

    def close_connection(self):
        # Send the disconnect tag to the server
        client_msg = "!DISCONNECT"
        print("[CLIENT-REQUEST]:", client_msg)
        self._instance._socket_connection.sendall(client_msg.encode('utf-8'))

        # Await for the server response for the previous tag.
        server_msg = self._instance._socket_connection.recv(8192)
        decoded_received = server_msg.decode('utf-8')
        print("[SERVER-RESPONSE]:", decoded_received)

    def transmit_to_server(self, to_encrypt):
        # Send tag to server to proceed with the next section of the code.
        client_msg = "!CONTINUE"
        encoded_send = client_msg.encode('utf-8')
        print("[CLIENT-REQUEST]:", client_msg)
        self._instance._socket_connection.send(encoded_send)

        # Await for the server to notify that the command was received.
        server_msg = self._instance._socket_connection.recv(8192)
        decoded_received = server_msg.decode('utf-8')
        print("[SERVER-RESPONSE]:", decoded_received)

        # Proceed on communicating using encryption
        # Send message to server
        cypher = encryptor.encrypt_message(to_encrypt, self._instance._server_public_key)
        self._instance._socket_connection.sendall(cypher)

        # Await for the encrypted server response
        cypher = self._instance._socket_connection.recv(8192)

        message = encryptor.decrypt_message(cypher, self._instance._client_private_key)
        print("[SERVER-RESPONSE]:", message)

        # Return the message back to the calling function.
        return message

    def receive_from_server(self, inbound):
        message = encryptor.decrypt_message(inbound, self._instance._client_private_key)

    def handle_server(self):
        pass
        # def handle_server(self):
        #     # This function is just a sequential execution block written in order to test
        #     # the server backend connection, key distribution and the transmission of a ciphertext
        #
        #     # Establish a connection to the server.
        #     print("Establishing connection to the server")
        #     if self._instance._client_priv_key is None:
        #         print("true")
        #     self._instance._socket_conn = socket.socket()
        #     self._instance._socket_conn.connect((SERVER_IP, SERVER_PORT))
        #
        #     # Send the following tag onto the open socket.
        #     client_msg = '!START'
        #     print("[CLIENT-REQUEST]:", client_msg)
        #     self._instance._socket_conn.send(client_msg.encode('utf-8'))
        #
        #     # Await for the server response to continue.
        #     server_msg = self._instance._socket_conn.recv(2048)
        #     print("[SERVER-RESPONSE]:", server_msg)
        #
        #     # Send the client public key from the current session to the server.
        #     key = self._instance._client_priv_key.public_key().public_bytes(
        #         encoding=encryptor.serialization.Encoding.PEM,
        #         format=encryptor.serialization.PublicFormat.SubjectPublicKeyInfo
        #     )
        #     self._instance._socket_conn.sendall(key)
        #
        #     # Await for the server to provide a session public key back.
        #     server_msg = self._instance._socket_conn.recv(8192)
        #     self._instance._server_pub_key = encryptor.serialization.load_pem_public_key(server_msg,
        #                                                                                 backend=encryptor.default_backend())
        #     print("[SERVER-RESPONSE]:", server_msg)
        #     self._instance.set_spublic_key(server_msg)
        #
        #     # Send tag to server to notify that the keys were received.
        #     client_msg = '!RECEIVED'
        #     print("[CLIENT-REQUEST]:", client_msg)
        #     self._instance._socket_conn.sendall(client_msg.encode('utf-8'))
        #
        #     # Await for the server response for the previous tag.
        #     server_msg = self._instance._socket_conn.recv(8192)
        #     decoded_received = server_msg.decode('utf-8')
        #     print("[SERVER-RESPONSE]:", decoded_received)
        #
        #     # Send tag to server to proceed with the next section of the code.
        #     client_msg = "!CONTINUE"
        #     encoded_send = client_msg.encode('utf-8')
        #     print("[CLIENT-REQUEST]:", client_msg)
        #     self._instance._socket_conn.send(encoded_send)
        #
        #     # Await for the server to notify that the command was received.
        #     server_msg = self._instance._socket_conn.recv(8192)
        #     decoded_received = server_msg.decode('utf-8')
        #     print("[SERVER-RESPONSE]:", decoded_received)
        #
        #     # Proceed on communicating using encryption
        #     # Send message to server
        #     toEncrypt = "hey there, this is the client"
        #     toEncode = encryptor.encrypt_msg(toEncrypt, self._instance._server_pub_key)
        #     self._instance._socket_conn.sendall(toEncode)
        #
        #     # Await for the encrypted server response
        #     toReceive = self._instance._socket_conn.recv(8192)
        #     # toDecode = toReceive.decode('utf-8')
        #     toDecrypt = encryptor.decrypt_msg(toReceive, self._instance._client_priv_key)
        #     print("[SERVER-RESPONSE]:", toDecrypt)
        #
        #     # Send the disconnect tag to the server
        #     client_msg = "!DISCONNECT"
        #     print("[CLIENT-REQUEST]:", client_msg)
        #     self._instance._socket_conn.sendall(client_msg.encode('utf-8'))
        #
        #     # Await for the server response for the previous tag.
        #     server_msg = self._instance._socket_conn.recv(8192)
        #     decoded_received = server_msg.decode('utf-8')
        #     print("[SERVER-RESPONSE]:", decoded_received)


def get_access_point_instance():
    return access_point()
