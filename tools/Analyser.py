

class Analyser:

    '''
        Analizer supports analysis on texts
            - Frequency Analysis
            - TANSMAT Analysis
    '''
    __text = ""

    def setText(self, text):
        self.__text = text

    '''
        Returns all occuring (ascii) letters and their number of occurances in the text
        sorted by descending frequency
    '''
    def getLetters(self,length=1):
        result = {}
        for i in [self.__text[i:i+length] for i in range(0, len(self.__text)-length)]:
            if i not in result:
                result[i] = 0
                
            result[i] += 1
        return sorted(result.items(), key=lambda item: item[1],reverse=True)

    '''
        Returns all divisors of a given number

        Can be used to determine e.g. the key of a TRANSMAT encrypted cipher
    '''
    def divider(self, num):
        div = []

        for i in range(1,num + 1):
            if num%i == 0:
                div.append(i)
        return div

    '''
        Returns all repetitive substrings of length > 3

        Can be used for Kasiski test e.g. determine the keylength of stream cyphers
    '''
    def getSubstrings(self):
        result = []
        prev = ""
        for i in range(len(self.__text)-1):
            for j in range(i+1,len(self.__text)):
                if self.__text[i] == self.__text[j]:
                    s = self.__text[i]
                    l = 1
                    while (j+l)<len(self.__text) and (self.__text[i+l] == self.__text[j+l]):
                        s += self.__text[i+l]
                        l += 1
                    if (l > 3):
                        if prev[1:] != s:
                            result.append((s, i, j, j-i))
                        prev = s
        return result

    def commonDividers(self):
        dividers = list(map(lambda a: self.divider(a[3]),self.getSubstrings()))
        result = {}
        for l in dividers:
            for d in l:
                if d not in result:
                    result[d] = 0
                    
                result[d] += 1
        return sorted(result.items(), key=lambda item: item[1],reverse=True)

    def euclidGCD(self,a,b):
        a=[a,b]
        way = []
        while a[-1]>0:
            step = []
            a.append(a[-2]%a[-1])

            step.append(a[-3])
            step.append(a[-3]//a[-2])
            step.append(a[-2])
            step.append(a[-1])
            way.append(step)
        return way
