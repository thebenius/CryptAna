
class VERNAM:

    '''
        VERNAM encrypts and decrypts VERNAM ciphers.
    '''

    __key = "11010"
    __text = "0011100101"

    def setKey(self, key):
        self.__key = key

    def getKey(self):
        return self.__key

    def setText(self,text):
        self.__text = text

    def encrypt(self):
        key = list(self.__key)
        text = list(self.__text)
        cipher = ""
        n = min(len(key),len(text))

        for i in range(n):
            cipher += str((int(key[i]) + int(text[i]))%2)

        if n < len(text):
            cipher += "".join(text[:len(text)])

        return cipher

    

