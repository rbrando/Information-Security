import sys
import base64
import os
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

key = RSA.generate(2048, Random.new().read)

class Alice:

    def writefile(self, input):
        file = open("ctext", "a")
        file.write(str(input))
        print("WriteFile - " + str(input))
        file.close()

    def encrypt(self, input):
        publicKey = key.publickey()

        #Encrypt message
        return publicKey.encrypt(input, 64)

class Bob:
    def readfile(self):
        file = open("ctext", "r")
        ctext = file.read()
        print("readFile - " + str(ctext))
        file.close()
        return ctext

    def decrypt(self, input):
        decrypt = key.decrypt(ast.literal_eval(str(input)))
        return decrypt

    def unpad(self, unpad):
        unpad = unpad.rstrip(b"\0")
        return unpad

def main(input):
    os.remove("./ctext")
    alice = Alice()
    ctext = alice.encrypt(input.encode())
    alice.writefile(ctext)

    bob = Bob()
    msg = bob.readfile()
    text = bob.decrypt(msg)
    print("Return: " + str(text))


enter = input("Please type a message to Encrypt: ")
main(enter)
