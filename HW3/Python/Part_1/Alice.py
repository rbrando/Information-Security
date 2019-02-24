import sys
import base64
from Crypto.Cipher import AES
from Crypto import Random

class Alice:

    def writefile(self, input):
        file = open("ctext", "wb")
        file.write(input)
        print("WriteFile - " + str(input))
        file.close()

    def encrypt(self, input):
        key = 'feeeecfdekfbvelj'
        key = str.encode(key)

        iv = Random.new().read(AES.block_size)

        # Pad input;
        msg = self.pad(input)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        #Encrypt message into base64 and with cipher
        return iv + cipher.encrypt(msg)


    def pad(self, padded):
        how_many = AES.block_size - len(padded) % AES.block_size
        return padded + b"\0" * how_many

def main(input):
    alice = Alice()
    ctext = alice.encrypt(input.encode())
    alice.writefile(ctext)


enter = input("Please type a message to Encrypt: ")
main(enter)
