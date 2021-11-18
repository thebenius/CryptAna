
class STREAM:

    _alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _key = ""
    _text = ""
    _cipher = ""

    def setKey(self, key):
        self._key = key

    def setText(self, text):
        self._text = text
    
    def setCipher(self, cipher):
        self._cipher = cipher

    def getKey(self, index):
        keylen = len(self._key)
        if (index < keylen):
            return list(self._alphabeth).index(self._key[index])
        else:
            return 0

    def encrypt(self):
        cipher = ""
        for i in range(len(self._text)):
            if not self._text[i] in self._alphabeth:
                cipher += self._text[i]
                continue
            a = list(self._alphabeth).index(self._text[i])
            k = self.getKey(i)
            cipher += self._alphabeth[(a+k)%len(self._alphabeth)]
        
        return cipher

    def decrypt(self):
        self._text = ""
        for i in range(len(self._cipher)):
            if not self._cipher[i] in self._alphabeth:
                self._text += self._cipher[i]
                continue
            a = list(self._alphabeth).index(self._cipher[i])
            k = self.getKey(i)
            self._text += self._alphabeth[(a-k)%len(self._alphabeth)]
        
        return self._text