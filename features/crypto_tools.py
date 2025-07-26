from Crypto.Cipher import AES
import base64
import hashlib

def encrypt(text, key):
    key = hashlib.sha256(key.encode()).digest()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())
    return base64.b64encode(nonce + ciphertext).decode()

def decrypt(cipher_text, key):
    try:
        key = hashlib.sha256(key.encode()).digest()
        data = base64.b64decode(cipher_text.encode())
        nonce = data[:16]
        ciphertext = data[16:]
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        decrypted = cipher.decrypt(ciphertext).decode()
        return decrypted
    except Exception as e:
        return f"❌ خطأ في فك التشفير: {str(e)}"
