import sys
import base64
from Crypto.Hash import HMAC, SHA256
from Crypto import Random

class Alice:

    def writefile(self, input):
        file = open("ctext", "w")
        file.write(input)
        print("WriteFile - " + str(input))
        file.close()

    def generateHMAC(self, message, key):
        h = HMAC.new(message, digestmod=SHA256)
        h.update(message)
        print(h.hexdigest())
        return h


    def encrypt(self, input):
        key = 'feeeecfdekfbvelj'
        key = str.encode(key)

        signature = self.generateHMAC(input, key)

        return str(signature.hexdigest()) + "\n" + str(input)

def main(input):
    alice = Alice()
    ctext = alice.encrypt(input.encode())
    alice.writefile(ctext)


enter = input("Please type a message to Encrypt: ")
main(enter)
