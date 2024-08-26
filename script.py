from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os

KEY = b'k\x16\xf17\x00\xf1\xd0\x0c\x03m:\xeb9\xf1\xd5N'
IV = os.urandom() 

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
