"""
    Date created:   01/10/2023
    Date edited:    04/17/2023
    Sub-module:     ap_handler.py
    Remarks:        This submodule contains the access point handler blueprint to be used in threads when
                    a new connection to a client has been established.
"""


# Imports
import server.src.utilities.cryp_functions as encryptor


class connectionRequestHandler:
    def __init__(self, inboundSocket, inboundAddress):
        self._serverPrivateKey = None
        self._serverPublicKey = None
        self._clientPublicKey = None
        self._clientSocket = inboundSocket
        self._clientAddress = inboundAddress
        self.bufferSize = 4096
        self.isAlive = True
        self.encodedInbound = None
        self.decodedInbound = None
        self.inputBuffer = None
        self.encodedOutbound = None
        self.decodedOutbound = None
        self._generateServerSessionKeys()

    # Server's private and public keys getters, and client public key getter
    def getServerPrivateKey(self):
        return self._serverPrivateKey

    def getServerPublicKey(self):
        return self._serverPublicKey

    def getClientPublicKey(self):
        return self._clientPublicKey

    # Key generator method
    def _generateServerSessionKeys(self):
        self._serverPrivateKey, self._serverPublicKey = encryptor.generate_key_pair()

    # Server public Key setter

    def setClientPublicKey(self, newClientPublicKey):
        self._clientPublicKey = newClientPublicKey

    def requestHandler(self):
        inbound = ""
        input_buffer = ""
        outbound = ""
        decoded_inbound = ""
        decoded_outbound = ""

        try:
            while self.isAlive:
                # Receive the initial or next operation keyword
                inbound = self._clientSocket.recv(self.bufferSize)
                decoded_inbound = inbound.decode('utf-8')
                print("[CLIENT-RESPONSE]:", str(decoded_inbound))

                decoded_outbound = "!REQUEST_RECEIVED"
                outbound = decoded_outbound.encode('utf-8')
                self._clientSocket.send(outbound)

                if decoded_inbound == "!START":
                    # Receive the public key from the client
                    inbound = self._clientSocket.recv(self.bufferSize)
                    received_key = encryptor.serialization.load_pem_public_key(inbound,
                                                                               backend=encryptor.default_backend())
                    print("[THREAD-INFO] Public Key Received:", str(received_key))
                    self.setClientPublicKey(received_key)

                    # Serialize the public key into PEM format
                    outbound = self._serverPrivateKey.public_key().public_bytes(
                        encoding=encryptor.serialization.Encoding.PEM,
                        format=encryptor.serialization.PublicFormat.SubjectPublicKeyInfo
                    )

                    # Send the server public keys to the client
                    self._clientSocket.sendall(outbound)
                    print("[THREAD-INFO] Public Key Sent:", self._serverPublicKey)

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
                    inbound = self._clientSocket.recv(self.bufferSize)

                    # Decrypt the decoded message using the encryptor class
                    client_msg = encryptor.decrypt_msg(inbound, self._serverPrivateKey)

                    # Handle client Message
                    print("[THREAD-INFO] Message received:", client_msg)

                    # Formulate the server response
                    server_msg = "Information received!"

                    # Encrypt the server response using the encryptor
                    # decoded_outbound = encryptor.encrypt_msg(server_msg, self.get_sprivate_key())
                    outbound = encryptor.encrypt_msg(server_msg, self._clientPublicKey)
                    # Encode using b64Encoder
                    # outbound = decoded_outbound.encode('utf-8')

                    # Send to client through the socket connection
                    self._clientSocket.sendall(outbound)

                elif decoded_inbound == "!DISCONNECT":
                    # Close the  connection and terminate the thread
                    print("[THREAD-INFO] Terminating client connection")
                    self._clientSocket.close()
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
                if self._clientSocket.fileno() >= 0:
                    self._clientSocket.close()
            except OSError:
                pass

    def close_c_connection(self):
        pass
        # Close connection Logic

    def transmit_to_client(self, message):
        out_bound = encryptor.encrypt_msg(message, self.getClientPublicKey())

        # Socket Transmission Logic here

    def receive_from_client(self, inbound):
        message = encryptor.decrypt_msg(inbound, self.getServerPrivateKey())
