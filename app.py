from flask import Flask, render_template, request
import hashlib
import os

app = Flask(__name__)

from aeshmac import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate-hmac-sha256', methods=['POST'])
def calculate_hmac_sha256():
    aes_encrypted_text = request.form['aes_encrypted_text']
    hmac_key = request.form['hmac_key']
    hash_value = generate_hmac_sha256(hmac_key,aes_encrypted_text)
    return render_template('result.html', aes_encrypted_text=aes_encrypted_text, hmac_key=hmac_key, hash_value=hash_value)


if __name__ == '__main__':
    app.run(debug=True)
