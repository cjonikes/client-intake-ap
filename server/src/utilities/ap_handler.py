"""
    Date created:   01/10/2023
    Date edited:    04/19/2023
    Sub-module:     ap_handler.py
    Remarks:        This submodule contains the access point handler blueprint to be used in threads when
                    a new connection to a client has been established.
"""

# Imports
import server.src.utilities.cryp_functions as encryptor
import server.src.utilities.server_logic as server_logic


class connection_request_handler:
    def __init__(self, inbound_socket, inbound_address):
        self._server_private_key = None
        self._server_public_key = None
        self._client_public_key = None
        self._client_socket = inbound_socket
        self._client_address = inbound_address
        self.buffer_size = 4096
        self.is_alive = True
        self.encoded_inbound = None
        self.decoded_inbound = None
        self.input_buffer = None
        self.encoded_outbound = None
        self.decoded_outbound = None
        self._generate_server_session_keys()

    # Server's private and public keys getters, and client public key getter
    def get_server_private_key(self):
        return self._server_private_key

    def get_server_public_key(self):
        return self._server_public_key

    def get_client_public_key(self):
        return self._client_public_key

    # Key generator method
    def _generate_server_session_keys(self):
        self._server_private_key, self._server_public_key = encryptor.generate_key_pair()

    # Server public Key setter

    def set_client_public_key(self, new_client_public_key):
        self._client_public_key = new_client_public_key

    def request_handler(self):
        encoded_inbound = ""
        encoded_outbound = ""
        decoded_inbound = ""
        decoded_outbound = ""

        try:
            while self.is_alive:
                # Receive the initial or next operation keyword
                encoded_inbound = self._client_socket.recv(self.buffer_size)
                decoded_inbound = encoded_inbound.decode('utf-8')
                print("[CLIENT-RESPONSE]:", str(decoded_inbound))

                decoded_outbound = "!REQUEST_RECEIVED"
                encoded_outbound = decoded_outbound.encode('utf-8')
                self._client_socket.send(encoded_outbound)

                if decoded_inbound == "!START":
                    # Receive the public key from the client
                    encoded_inbound = self._client_socket.recv(self.buffer_size)
                    received_key = encryptor.serialization.load_pem_public_key(encoded_inbound,
                                                                               backend=encryptor.default_backend())
                    print("[THREAD-INFO] Public Key Received:", str(received_key))
                    self.set_client_public_key(received_key)

                    # Serialize the public key into PEM format
                    encoded_outbound = self._server_private_key.public_key().public_bytes(
                        encoding=encryptor.serialization.Encoding.PEM,
                        format=encryptor.serialization.PublicFormat.SubjectPublicKeyInfo
                    )

                    # Send the server public keys to the client
                    self._client_socket.sendall(encoded_outbound)
                    print("[THREAD-INFO] Public Key Sent:", self._server_public_key)

                elif decoded_inbound == "!RECEIVED":
                    print("[THREAD-INFO] Both keys where exchanged successfully with client")

                elif decoded_inbound == "!CONTINUE":
                    # Proceed into an encrypted communication
                    # Receive from the server an encoded message or '!EXIT'
                    encoded_inbound = self._client_socket.recv(self.buffer_size)

                    # Decrypt the decoded message using the encryptor class
                    client_message_json = self.cypher_processor('d', encoded_inbound)

                    # Handle client Message
                    print("[THREAD-INFO] Message received:", client_message_json)

                    # Send the client message (JSON) to the server logic for processing and await for result (JSON)
                    server_message_json = server_logic.operation_selector(client_message_json)
                    print("[THREAD-INFO] Message to send:", server_message_json)

                    # Encrypt the server response using the encryptor
                    encoded_outbound = self.cypher_processor('e', server_message_json)

                    # Send to client through the socket connection
                    self._client_socket.sendall(encoded_outbound)
                    print("[THREAD-INFO] Message sent!")

                elif decoded_inbound == "!DISCONNECT":
                    # Close the  connection and terminate the thread
                    print("[THREAD-INFO] Terminating client connection")
                    self._client_socket.close()
                    self.is_alive = False

                else:
                    # Handle the case where the received keyword is not "!START"
                    print("[THREAD-INFO] Unexpected keyword received:", decoded_inbound)

                encoded_inbound = ""
                encoded_outbound = ""
                decoded_inbound = ""
                decoded_outbound = ""

        except Exception as e:
            print(f"[THREAD-ERROR] {str(e)}")
        finally:
            try:
                if self._client_socket.fileno() >= 0:
                    self._client_socket.close()
            except OSError:
                pass

    def close_current_connection(self):
        pass
        # Close connection Logic

    def cypher_processor(self, operation_type, unprocessed_message):
        match operation_type:
            case 'e':
                # Encrypts the original message.
                processed_message = encryptor.encrypt_msg(unprocessed_message, self.get_client_public_key())
            case 'd':
                # Decrypts the original message.
                processed_message = encryptor.decrypt_msg(unprocessed_message, self.get_server_private_key())
            case _:
                processed_message = ''
                print("[THREAD-ERROR] No message was processed.")

        return processed_message
