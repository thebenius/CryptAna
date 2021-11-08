
class VIGENERE:

    __alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __key = ""
    __text = ""
    __cipher = ""

    def setKey(self, key):
        self.__key = key

    def setText(self, text):
        self.__text = text
    
    def setCipher(self, cipher):
        self.__cipher = cipher

    def encrypt(self):
        cipher = ""
        for i in range(len(self.__text)):
            if not self.__text[i] in self.__alphabeth:
                cipher += self.__text[i]
                continue
            a = list(self.__alphabeth).index(self.__text[i])
            k = list(self.__alphabeth).index(self.__key[i%len(self.__key)])
            cipher += self.__alphabeth[(a+k)%len(self.__alphabeth)]
        
        return cipher

    def decrypt(self):
        text = ""
        for i in range(len(self.__cipher)):
            if not self.__cipher[i] in self.__alphabeth:
                text += self.__cipher[i]
                continue
            a = list(self.__alphabeth).index(self.__cipher[i])
            k = list(self.__alphabeth).index(self.__key[i%len(self.__key)])
            text += self.__alphabeth[(a-k)%len(self.__alphabeth)]
        
        return text