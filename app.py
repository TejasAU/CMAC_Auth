from flask import Flask, render_template, request
from Crypto.Hash import CMAC
from Crypto.Cipher import AES
from aeshmac import *
from aescbcmac import *
from aesgmac import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate-macs', methods=['POST'])
def calculate_macs():
    aes_encrypted_text = request.form['aes_encrypted_text']
    key = request.form['key']
    mac_algorithm = request.form['mac_algorithm']
    
    if mac_algorithm == 'hmac_sha256':
        hash_value = generate_hmac_sha256(key, aes_encrypted_text)
    elif mac_algorithm == 'cbc_mac_aes':
        key, hash_value = generate_cbc_mac_aes(aes_encrypted_text)
    elif mac_algorithm == 'gmac_aes':
        key, hash_value = generate_gmac_aes(aes_encrypted_text)
    else:
        key, hash_value = "", "Invalid MAC algorithm selected"

    return render_template('result.html', aes_encrypted_text=aes_encrypted_text, key=key, mac_algorithm=mac_algorithm, hash_value=hash_value)

if __name__ == '__main__':
    app.run(debug=True)
