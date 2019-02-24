import sys
import base64
from Crypto.Cipher import AES
from Crypto import Random

class Alice:

    def writefile(self, input):
        file = open("ctext", "wb")
        file.write(input)
        print("WriteFile - " + input.decode())

    def encrypt(self, input):
        key = 'feeeecfdekfbvelj'
        key = str.encode(key)

        iv = Random.new().read(AES.block_size)

        # Pad input; bytes
        msg = self.pad(input).encode()

        cipher = AES.new(key, AES.MODE_CBC, iv)

        #Encrypt message into base64 and with cipher
        return base64.b64encode(cipher.encrypt(msg))


    def pad(self, padded):
        str_length = 16 - (len(padded) % 16)
        padded = padded + (chr(str_length)*str_length)
        print("padding: " + str(len(padded)))
        return padded

def main(input):
    alice = Alice()
    ctext = alice.encrypt(input)
    alice.writefile(ctext)


enter = input("Enter a message to Encrypt: ")
main(enter)
