
from tools.Base import Base

class FIXEDXOR:

    __key = Base()
    __text = Base()

    def setKey(self, key):
        self.__key = key

    def setText(self, text):
        self.__text = text

    def encrypt(self):
        return self.__text.getInt() ^ self.__key.getInt()
    
    