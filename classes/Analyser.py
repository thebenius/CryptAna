

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
    def getLetters(self):
        result = {}
        for i in self.__text:
            if i not in result:
                result[i] = 0
                
            result[i] += 1
        return sorted(result.items(), key=lambda item: item[1],reverse=True)

    '''
        Returns all divisors of a given number

        Can be used to determine e.g. the key of a TRANSMAT encrypted cipher
    '''
    def divider(num):
        div = []

        for i in range(1,num + 1):
            if num%i == 0:
                div.append(i)
        return div