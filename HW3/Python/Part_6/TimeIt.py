import timeit
from Crypto.Cipher import AES
from Crypto import Random
import base64
import sys
import os
from Crypto.PublicKey import RSA
from Crypto.Hash import HMAC, SHA256
import ast

#RSA
key = RSA.generate(2048, Random.new().read)
private_key = key.exportKey()
public_key = key.publickey().exportKey()
global hash

class RSA_Alice:

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

class RSA_Bob:

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
            #print("Valid key")
        except TypeError:
            i = 0
            #print ("Invalid key")
        return input

    def unpad(self, unpad):
        unpad = unpad.rstrip(b"\0")
        return unpad

def RSA_main(input):
    print("RSA Timings - ")
    os.remove("./ctext")
    alice = RSA_Alice()
    average_time = 0
    for i in range(100):
        start = timeit.timeit()
        ctext = alice.encrypt(input.encode())
        end = timeit.timeit()
        average_time = average_time + (abs(end - start))
    print("Average Encryption Time: " + str(average_time/100))
    alice.writefile(ctext)

    bob = RSA_Bob()
    average_time = 0
    msg = bob.readfile()
    for i in range(100):
        start = timeit.timeit()
        text = bob.decrypt(msg)
        end = timeit.timeit()
        average_time = average_time + (abs(end - start))
    print("Average Decryption Time: " + str(average_time/100))
    #print("Return: " + str(text))

#AES
class AES_Alice:

    def writefile(self, input):
        file = open("ctext", "w")
        file.write(input)
        #print("WriteFile - " + str(input))
        file.close()

    def generateHMAC(self, message, key):
        h = HMAC.new(message, digestmod=SHA256)
        h.update(message)
        #print(h.hexdigest())
        return h


    def encrypt(self, input):
        key = 'feeeecfdekfbvelj'
        key = str.encode(key)

        signature = self.generateHMAC(input, key)

        return str(signature.hexdigest()) + "\n" + str(input)

class AES_Bob:

    mac = None

    def readfile(self):
        file = open("ctext", "rb")
        ctext = file.readlines()
        mac = file.readlines(2)
        #print("readFile - " + str(mac) + str(ctext))
        file.close()
        return ctext, mac

    def verifysignature(self, key, input, mac):
        h = HMAC.new(key, digestmod=SHA256)
        h.update(input.encode())
        try:
            i = 1
                #print("The message " + str(input) + "is valid")
        except ValueError:
            i = 0
            #print("The message or key is wrong")

    def decrypt(self, input, mac):
        key = 'feeeecfdekfbvelj'
        key = str.encode(key)

        self.verifysignature(key,input,mac)

        return input
def AES_main(input):
    print("HMAC Times - ")
    alice = AES_Alice()
    average_time = 0
    for i in range(100):
        start = timeit.timeit()
        ctext = alice.encrypt(input.encode())
        end = timeit.timeit()
        average_time = average_time + (abs(end - start))
    print("Average Encryption Time: " + str(average_time/100))
    alice.writefile(ctext)

    bob = AES_Bob()
    average_time = 0
    msg, mac = bob.readfile()
    for i in range(100):
        start = timeit.timeit()
        text = bob.decrypt(str(msg), mac)
        end = timeit.timeit()
    average_time = average_time + (abs(end - start))
    print("Average Decryption Time: " + str(average_time/100))
    #print("Return: " + str(text))


enter = input("Please type a message to Encrypt: ")
RSA_main(enter)
AES_main(enter)
