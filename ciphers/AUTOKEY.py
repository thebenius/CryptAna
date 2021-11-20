from .STREAM import STREAM

class AUTOKEY(STREAM):

    def getKey(self, index):
        keylen = len(self._key)
        if (index < keylen):
            return list(self._alphabeth).index(self._key[index])
        else:
            return list(self._alphabeth).index(self._text[index-keylen])
