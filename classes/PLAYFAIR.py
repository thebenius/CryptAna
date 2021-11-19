
class PLAYFAIR:

    __alphabeth = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    __key = ""
    __text = ""
    __cipher = ""

    def setKey(self, key):
        for l in key+self.__alphabeth:
            if l not in self.__key and l in self.__alphabeth:
                self.__key += l

    def getKey(self):
        return self.__key

    def getI(self, letter):
        return list(self.__key).index(letter)//5

    def getJ(self, letter):
        return list(self.__key).index(letter)%5

    def getLetter(self, i,j):
        return self.__key[(i%5)*5+(j%5)]

    def setText(self, text):
        previous = ""
        for l in text:
            if l not in self.__alphabeth:
                continue
            if previous != l:
                self.__text += l
            else:
                self.__text += "X"+l
                previous = ""
            if previous == "":
                previous = l
            else:
                previous = ""
        
        if previous != "":
            self.__text += "X"

    def setCipher(self, cipher):
        for l in cipher:
            if l in self.__alphabeth:
                self.__cipher += l

    def getCipher(self):
        return self.__cipher

    def encrypt(self):
        cipher = ""
        for tuple in [self.__text[i:i+2] for i in range(0, len(self.__text), 2)]:
            i1 = self.getI(tuple[0])
            j1 = self.getJ(tuple[0])
            i2 = self.getI(tuple[1])
            j2 = self.getJ(tuple[1])
            if i1 == i2:
                cipher += self.getLetter(i1,j1+1) + self.getLetter(i2,j2+1)
            elif j1 == j2:
                cipher += self.getLetter(i1+1,j1) + self.getLetter(i2+1,j2)
            else:
                cipher += self.getLetter(i1, j2) + self.getLetter(i2,j1)
        return cipher

    def decrypt(self):
        text = ""
        for tuple in [self.__cipher[i:i+2] for i in range(0, len(self.__cipher), 2)]:
            i1 = self.getI(tuple[0])
            j1 = self.getJ(tuple[0])
            i2 = self.getI(tuple[1])
            j2 = self.getJ(tuple[1])
            if i1 == i2:
                text += self.getLetter(i1,j1-1) + self.getLetter(i2,j2-1)
            elif j1 == j2:
                text += self.getLetter(i1-1,j1) + self.getLetter(i2-1,j2)
            else:
                text += self.getLetter(i1, j2) + self.getLetter(i2,j1)
        return text