import sys
import base64
from Crypto.Cipher import AES

class Bob:

    def readfile(self):
        file = open("ctext", "rb")
        ctext = file.read()
        print("readFile - " + ctext.decode())
        return ctext

    def decrypt(self, input):
        key = 'feeeecfdekfbvelj'
        key = str.encode(key)

        msg = base64.b64decode(input)
        iv = msg[:AES.block_size]

        decipher = AES.new(key, AES.MODE_CBC, iv)
        return self.unpad(decipher.decrypt(msg[AES.block_size:])).decode('utf-8')


    def unpad(self, unpad):
        unpad = unpad#[:-unpad[-1]]
        return unpad

    def pad(self, padded):
        str_length = 16 - (len(padded) % 16)
        padded = padded + bytes([str_length])* str_length
        return padded

def main():
    bob = Bob()
    msg = bob.readfile()
    text = bob.decrypt(msg)
    print("Return: " + text)

main()
