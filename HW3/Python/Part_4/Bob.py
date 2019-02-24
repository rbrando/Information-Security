import sys
import base64
from Crypto.Hash import HMAC, SHA256
from Crypto import Random

class Bob:

    mac = None

    def readfile(self):
        file = open("ctext", "rb")
        ctext = file.readlines()
        mac = file.readlines(2)
        print("readFile - " + str(mac) + str(ctext))
        file.close()
        return ctext, mac

    def verifysignature(self, key, input, mac):
        h = HMAC.new(key, digestmod=SHA256)
        h.update(input)

        try:
            h.hexverify(mac.encode())
            print("The message " + str(input) + "is valud")
        except ValueError:
            print("The message or key is wrong")

    def decrypt(self, input, mac):
        key = 'feeeecfdekfbvelj'
        key = str.encode(key)

        self.verifysignature(key,input,mac)

        return input

def main():
    bob = Bob()
    msg, mac = bob.readfile()
    text = bob.decrypt(msg, mac)
    print("Return: " + str(text))

main()
