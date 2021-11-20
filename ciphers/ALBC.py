
class ALBC:

    '''
        ALBC encrypts and decrypts ALBC-2 ciphers.

        TODO implement ALBC-K
    '''

    __alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __key = (0,1,15,21,1,13)
    __text = ""

    def setKey(self, key):
        self.__key = key

    def setText(self,text):
        self.__text = text

    def encrypt(self):
        text = list(self.__text + self.__alphabeth[0]*(len(self.__text)%2))
        cipher = ""
        key = self.__key
        for i in range(len(text)//2):
            x = (ord(text[2*i])-65)
            y = (ord(text[2*i+1])-65)

            cipher += chr(((key[0]*x + key[1]*y + key[2])%26)+65)
            cipher += chr(((key[3]*x + key[4]*y + key[5])%26)+65)

        return cipher

    

