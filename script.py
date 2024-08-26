from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os

KEY = b'Not_Ready_To_Commit'
IV = os.urandom(16)

assert len(KEY) == 16
assert len(IV) == 16

def encrypt(plaintext, key, iv):
    padded = pad(plaintext, 16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded)
    return iv+ciphertext

def main():
    with open('location.png','rb') as file:
        data = file.read()
    encData = encrypt(data, KEY, IV)
    with open('encrypted.png', 'wb') as encFile: 
        encFile.write(encData)

if __name__ == "__main__":
    main()
