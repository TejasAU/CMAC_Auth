import hashlib
import os
import hmac

# Function to generate HMAC-SHA256 for encrypted data
def generate_hmac_sha256(key, hex_encrypted_data):
    # Convert hexadecimal encrypted data to bytes
    encrypted_data = bytes.fromhex(hex_encrypted_data)

    # Generate HMAC-SHA256 for encrypted data using key
    hmac_obj = hmac.new(key.encode('utf-8'), encrypted_data, hashlib.sha256)
    hmac_digest = hmac_obj.digest()
    return hmac_digest.hex()


