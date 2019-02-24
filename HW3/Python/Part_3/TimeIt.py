import timeit
from Crypto.Cipher import AES
from Crypto import Random
import base64
import sys
import os
from Crypto.PublicKey import RSA
import ast

#RSA
key = RSA.generate(2048, Random.new().read)
class RSA_Alice:

    def writefile(self, input):
        file = open("ctext", "a")
        file.write(str(input))
        #print("WriteFile - " + str(input))
        file.close()

    def encrypt(self, input):
        publicKey = key.publickey()

        #Encrypt message
        return publicKey.encrypt(input, 64)

class RSA_Bob:
    def readfile(self):
        file = open("ctext", "r")
        ctext = file.read()
        #print("readFile - " + str(ctext))
        file.close()
        return ctext

    def decrypt(self, input):
        decrypt = key.decrypt(ast.literal_eval(str(input)))
        return decrypt

    def unpad(self, unpad):
        unpad = unpad.rstrip(b"\0")
        return unpad

def RSA_main(input):
    os.remove("./ctext")
    print("RSA Times - ")
    average_time = 0
    alice = RSA_Alice()
    for i in range(100):
        start = timeit.timeit()
        ctext = alice.encrypt(input.encode())
        end = timeit.timeit()
        average_time = average_time + (abs(end - start))
    print("Average Encryption Time: " + str(average_time/100))
    alice.writefile(ctext)

    bob = RSA_Bob()
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
        file = open("ctext", "wb")
        file.write(input)
        #print("WriteFile - " + str(input))
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

class AES_Bob:

    def readfile(self):
        file = open("ctext", "rb")
        ctext = file.read()
        #print("readFile - " + str(ctext))
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

def AES_main(input):
    print("AES Times - ")
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
    msg = bob.readfile()
    for i in range(100):
        start = timeit.timeit()
        text = bob.decrypt(msg)
        end = timeit.timeit()
        average_time = average_time + (abs(end - start))
    print("Average Decryption Time: " + str(average_time/100))
    #print("Return: " + str(text))


enter = input("Please type a message to Encrypt: ")
RSA_main(enter)
AES_main(enter)
