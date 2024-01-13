"""
    Date created:   01/10/2023
    Date edited:    01/11/2023
    Sub-module:     ap_handler.py
    Remarks:        This submodule contains the access point handler blueprint to be used in threads when
                    a new connection to a client has been established.
"""


# Imports
import server.src.utilities.cryp_functions as encryptor


class client_handler:
    def __init__(self, conn, addr):
        self._server_priv_key = None
        self._server_pub_key = None
        self._client_pub_key = None
        self._client_socket = conn
        self._client_address = addr
        self._queue_manager_ref = None
        self.bufferSize = 4096
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

    def handle_connection(self):
        inbound = ""
        input_buffer = ""
        outbound = ""
        decoded_inbound = ""
        decoded_outbound = ""

        try:
            while self.isAlive:
                # Receive the initial or next operation keyword
                inbound = self._client_socket.recv(self.bufferSize)
                decoded_inbound = inbound.decode('utf-8')
                print("[CLIENT-RESPONSE]:", str(decoded_inbound))

                decoded_outbound = "!REQUEST_RECEIVED"
                outbound = decoded_outbound.encode('utf-8')
                self._client_socket.send(outbound)

                if decoded_inbound == "!START":
                    # Receive the public key from the client
                    inbound = self._client_socket.recv(self.bufferSize)
                    received_key = encryptor.serialization.load_pem_public_key(inbound,
                                                                               backend=encryptor.default_backend())
                    print("[THREAD-INFO] Public Key Received:", str(received_key))
                    self.set_cpublic_key(received_key)

                    # Serialize the public key into PEM format
                    outbound = self._server_priv_key.public_key().public_bytes(
                        encoding=encryptor.serialization.Encoding.PEM,
                        format=encryptor.serialization.PublicFormat.SubjectPublicKeyInfo
                    )

                    # Send the server public keys to the client
                    self._client_socket.sendall(outbound)
                    print("[THREAD-INFO] Public Key Sent:", self._server_pub_key)

                    # wait for the 'received' message from client
                    # inbound = self._client_socket.recv(self.bufferSize)
                    # decoded_inbound = inbound.decode('utf-8')
                    # print("[CLIENT-RESPONSE]:", str(decoded_inbound))

                elif decoded_inbound == "!RECEIVED":
                    print("[THREAD-INFO] Both keys where exchanged successfully with client")

                elif decoded_inbound == "!CONTINUE":
                    # Proceed into an encrypted communication
                    # while decoded_inbound != "!EXIT":
                    # Receive from the server a Base64 encoded message or '!EXIT'
                    inbound = self._client_socket.recv(self.bufferSize)

                    # Decrypt the decoded message using the encryptor class
                    client_msg = encryptor.decrypt_msg(inbound, self._server_priv_key)

                    # Handle client Message
                    print("[THREAD-INFO] Message received:", client_msg)

                    # Formulate the server response
                    server_msg = "Information received!"

                    # Encrypt the server response using the encryptor
                    # decoded_outbound = encryptor.encrypt_msg(server_msg, self.get_sprivate_key())
                    outbound = encryptor.encrypt_msg(server_msg, self._client_pub_key)
                    # Encode using b64Encoder
                    # outbound = decoded_outbound.encode('utf-8')

                    # Send to client through the socket connection
                    self._client_socket.sendall(outbound)

                elif decoded_inbound == "!DISCONNECT":
                    # Close the  connection and terminate the thread
                    print("[THREAD-INFO] Terminating client connection")
                    self._client_socket.close()
                    self.isAlive = False

                else:
                    # Handle the case where the received keyword is not "!START"
                    print("[THREAD-INFO] Unexpected keyword received:", decoded_inbound)

                inbound = ""
                input_buffer = ""
                outbound = ""
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

        # try:
        #     # Receive the public key from the client
        #     while Buffering:
        #         # Buffer the input
        #         inbound = self._client_socket.recv(self.bufferSize)
        #         if not inbound:
        #             Buffering = False
        #         else:
        #             self.inputBuffer += inbound
        #
        #     self.set_cpublic_key(self.inputBuffer)
        #     self.inputBuffer = ""
        #     # Send the server public keys to the client
        #     self._client_socket.sendAll(self.get_spublic_key())
        #
        #     while Received != "!DISCONNECT":

    def close_c_connection(self):
        pass
        # Close connection Logic

    def transmit_to_client(self, message):
        out_bound = encryptor.encrypt_msg(message, self.get_cpublic_key())

        # Socket Transmission Logic here

    def receive_from_client(self, inbound):
        message = encryptor.decrypt_msg(inbound, self.get_sprivate_key())
