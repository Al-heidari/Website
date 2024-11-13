from flask import Flask, request, jsonify
from flask_cors import CORS
from aes_module import Encryption_AES, Decryption_AES

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# PKCS7 Padding function
def pad(text, block_size=16):
    padding_length = block_size - (len(text) % block_size)
    return text + chr(padding_length) * padding_length

# PKCS7 Unpadding function
def unpad(text):
    padding_length = ord(text[-1])
    return text[:-padding_length]

@app.route('/aes', methods=['POST'])
def aes_process():
    try:
        data = request.json
        text = data['text']
        key = data['key']
        key_size = int(data['keySize'])
        action = data['action']

        print("Received data:", data)

        # Ensure the key length matches the specified key size
        required_key_length = key_size // 8
        if len(key) != required_key_length:
            return jsonify(output=f"Error: Key must be {required_key_length} characters long for {key_size}-bit AES."), 400

        # Convert key to bytes
        key_bytes = [ord(c) for c in key]

        # Add padding for encryption
        if action == 'encrypt':
            text = pad(text)  # Pad text to be a multiple of 16 bytes

        # Convert text to bytes
        text_bytes = [ord(c) for c in text]

        # Perform encryption or decryption
        if action == 'encrypt':
            aes = Encryption_AES(key_bytes)
            result_bytes = aes.cipher(text_bytes)
        elif action == 'decrypt':
            aes = Decryption_AES(key_bytes)
            result_bytes = aes.eq_inv_cipher(text_bytes)
            result = ''.join(chr(b) for b in result_bytes)
            result = unpad(result)  # Remove padding after decryption
            return jsonify(output=result)

        # Convert result bytes to a hexadecimal string for readability (for encryption)
        result = ''.join(f'{b:02x}' for b in result_bytes)
        print("Result:", result)
        return jsonify(output=result)
    except Exception as e:
        print("Error:", e)
        return jsonify(output="Error: " + str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
