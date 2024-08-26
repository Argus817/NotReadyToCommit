from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os

KEY = b'P455W0RD-0F-Argus817'
IV = b'u4\xb5\xc3/\xd0D\xfd\x0b\xf3\x05\x9b\xfa\xc3\xfck'

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
