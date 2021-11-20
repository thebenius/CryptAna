from .STREAM import STREAM

class VIGENERE(STREAM):

    def getKey(self, index):
        return list(self._alphabeth).index(self._key[index%len(self._key)])