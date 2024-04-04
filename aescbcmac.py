from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import secrets

def generate_cbc_mac_aes(hex_encrypted_data):
    # Convert hexadecimal encrypted data to bytes
    encrypted_data = bytes.fromhex(hex_encrypted_data)

    # Generate a random 32-byte AES key
    key = secrets.token_bytes(32)

    # Create an AES cipher object with the random key
    cipher = AES.new(key, AES.MODE_CBC, IV=bytes(16))

    # Pad the data to a multiple of 16 bytes
    padded_data = pad(encrypted_data, AES.block_size)

    # Calculate CBC-MAC for padded data using AES cipher
    cbc_mac = cipher.encrypt(padded_data)[-16:]
    return key.hex(), cbc_mac.hex()
