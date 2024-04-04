from Crypto.Cipher import AES
import hashlib
import secrets

def generate_gmac_aes(hex_encrypted_data):
    # Convert hexadecimal encrypted data to bytes
    encrypted_data = bytes.fromhex(hex_encrypted_data)

    # Generate a random nonce
    nonce = secrets.token_bytes(12)

    # Generate a random 32-byte AES key
    key = secrets.token_bytes(32)

    # Create an AES cipher object with the provided key and nonce
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    # Calculate GMAC for encrypted data using AES cipher
    cipher.update(encrypted_data)  # Include the encrypted data in the calculation
    gmac = cipher.digest()
    return key.hex(), gmac.hex()
