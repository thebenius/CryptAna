
class MASCer:

    '''
        MASCer
        This Class supports partial letter replacement to crack Replacement Ciphers.
    '''
    
    __text = ""
    __rules = {}

    def setText(self, text):
        self.__text = text

    def getResult(self):
        result = ""
        for c in self.__text:
            if c in self.__rules:
                c = self.__rules[c]
            else:
                c = c.lower()
            result += c
        return result

    '''
        Retreive the (concatenated partial) key of the cipher.

        This key may be wrong, if not every letter has a rule yet.
    '''
    def getKey(self):
        return "".join(list(map(lambda t: t[0],sorted(self.__rules.items(), key=lambda item: item[1]))))

    def addRule(self, key, value):
        self.__rules[key] = value

    
