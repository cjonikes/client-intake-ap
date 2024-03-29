"""
    Date created:   01/10/2024
    Date edited:    01/10/2024
    Sub-module:     cryp_functions.py
    Remarks:        This module is utilized to generate private and public keys for a session.
"""
import base64

# Imports
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import json


def generate_key_pair():
    """
        Remarks: This function generates the sessions private and public keys
    """
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    return private_key, public_key


def encrypt_msg(to_encrypt, server_public_key):
    """
        Remarks:
    """
    serialized_data = json.dumps(to_encrypt).encode('utf-8')
    encrypted_data = server_public_key.encrypt(
        serialized_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_data  # Encode the encrypted data for transmission (base64)


def decrypt_msg(to_decrypt, client_private_key):
    """
        Remarks:
    """
    # Decode the encrypted data in order to decrypt it

    decrypted_data = client_private_key.decrypt(
        to_decrypt,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    deserialized_data = json.loads((decrypted_data.decode('utf-8')))

    return deserialized_data

# #Unit Testing
# if __name__ == '__main__':
#
#     data = {'username': 'new_user123'}
#     pri_key, pub_key = generate_key_pair()
#
#     message = encrypt_msg(data, pub_key)
#     encoded_data = base64.b64encode(message)
#
# # Server
#     decoded_data = base64.b64decode(encoded_data)
#     new_message = decrypt_msg(decoded_data, pri_key)
#
#     print("\n", str(new_message))
