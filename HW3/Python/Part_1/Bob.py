import sys
import base64
from Crypto.Cipher import AES

class Bob:

    def readfile(self):
        file = open("ctext", "rb")
        ctext = file.read()
        print("readFile - " + str(ctext))
        file.close()
        return ctext

    def decrypt(self, input):
        key = 'feeeecfdekfbvelj'
        key = str.encode(key)


        iv = input[:AES.block_size]
        msg = input[AES.block_size:]

        decipher = AES.new(key, AES.MODE_CBC, iv)


        return self.unpad(decipher.decrypt(msg))


    def unpad(self, unpad):
        unpad = unpad.rstrip(b"\0")
        return unpad

def main():
    bob = Bob()
    msg = bob.readfile()
    text = bob.decrypt(msg)
    print("Return: " + str(text))

main()
