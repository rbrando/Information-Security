import sys
import base64
import os
from Crypto.PublicKey import RSA
from Crypto import Random
import Crypto.Hash.SHA256 as SHA256
import ast

key = RSA.generate(2048, Random.new().read)
private_key = key.exportKey()
public_key = key.publickey().exportKey()
global hash

class Alice:

    def writefile(self, input):
        file = open("ctext", "a")
        file.write(str(input))
        #print("WriteFile - " + str(input))
        file.close()

    def encrypt(self, input):
        alice_private_key = RSA.importKey(private_key)
        pub_key = RSA.importKey(public_key)
        hash = SHA256.new(input).digest()

        signature = key.sign(hash, Random.new().read)

        return str(signature) + "\n" + str(input)

class Bob:

    def __init__(self):
        file = open("ctext","r")
        self.sig = file.readline(2)
        file.close()

    def readfile(self):
        file = open("ctext", "r")
        ctext = file.readline(1)
        sig = file.readline(2)
        #print("readFile - " + str(ctext))
        file.close()
        return ctext

    def decrypt(self, input):
        #print(type(self.sig))
        try:
            key.verify(hash,self.sig)
            print("Valid key")
        except TypeError:
            print ("Invalid key")
        return input

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
    #print("Return: " + str(text))


enter = input("Please type a message to Encrypt: ")
main(enter)
