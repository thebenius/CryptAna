
class CAESAR:

    '''
        CAESAR is a simple class to encrypt or decrypt CAESAR ciphers.
    '''

    __alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __cipher = ""
    __text = ""
    __key = 0

    def getAlphabeth(self):
        return self.__alphabeth

    def setCipher(self, cipher):
        self.__cipher = cipher

    def getCipher(self):
        return self.__cipher

    def setText(self, text):
        self.__text = text

    def getText(self):
        return self.__text

    def setKey(self, key):
        self.__key = key

    def getKey(self):
        return self.__key

    def decrypt(self):
        self.__text = ""

        for c in self.__cipher:
            if c in self.__alphabeth:
                i = (self.__alphabeth.index(c) - self.__key) % len(self.__alphabeth)
                c = self.__alphabeth[i]
            self.__text += c