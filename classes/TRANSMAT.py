from random import seed
from random import choice
import time

class TRANSMAT:

    '''
        TRANSMAT encrypts and decrypts TRANSMAT ciphers.
    '''

    __text = ""
    __cipher = ""
    __key = (0,0)

    def setText(self,text):
        self.__text = text

    def setCipher(self,cipher):
        self.__cipher = cipher

    def setKey(self,key):
        self.__key = key
    
    def getText(self):
        return self.__text
    
    def getCipher(self):
        return self.__cipher

    def encrypt(self):
        seed(time.time())
        keylen = (self.__key[0]*self.__key[1])
        padding = len(self.__text)%keylen
        if padding != 0:
            padding = keylen - padding
        plaintext = self.__text
        while padding > 0:
            plaintext += choice(self.__text)
            padding -= 1

        numchunks = len(plaintext)//keylen
        chunks = [plaintext[i*keylen:(i+1)*keylen] for i in range(numchunks)]
        
        cipher = ""

        for chunk in chunks:
            for n in range(self.__key[1]):
                for m in range(self.__key[0]):
                    cipher += chunk[m*self.__key[1]+n]

        self.__cipher = cipher

    def decrypt(self):
        self.__text = ""

        seed(time.time())
        keylen = (self.__key[0]*self.__key[1])
        cipher = self.__cipher
        if len(self.__text)%keylen != 0:
            print("ERROR! Not the right Key!")

        numchunks = len(cipher)//keylen
        chunks = [cipher[i*keylen:(i+1)*keylen] for i in range(numchunks)]

        plaintext = ""

        for chunk in chunks:
            for n in range(self.__key[0]):
                for m in range(self.__key[1]):
                    plaintext += chunk[m*self.__key[0]+n]

        self.__text = plaintext