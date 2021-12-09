
class Base:
    '''
        This class takes a set of digits representing the digits of a base<N> system.
        You can then perform operations on numbers(instances) in this system.
    '''

    __digits = "0123456789ABCDEF"
    __number = "0"
    _casing = False

    def __init__(self, digits="0123456789ABCDEF", num="0"):
        self.__digits = digits
        self.__number = num


    def __str__(self):
        return self.__number

    def getDigit(self, digit):
        if digit >= self.getBase() or digit < 0:
            return 0
        return self.__digits[digit]

    def index(self, digit):
        return (self.__digits.index(digit) if self._casing else self.__digits.index(digit.upper()))

    def getBase(self):
        return len(self.__digits)

    def setNumber(self, number):
        self.__number = number


    def getInt(self):
        result = 0
        for digit in self.__number:
            result *= self.getBase()
            result += self.index(digit)
        return result

    def setInt(self, number):
        result = ""
        while number != 0:
            result = self.getDigit(number%self.getBase()) + result
            number //= self.getBase()
        self.__number = result
        


class Base2(Base):
    def __init__(self, num="0"):
        Base.__init__(self,"01", num)


class Base8(Base):
    def __init__(self, num="0"):
        Base.__init__(self,"01234567", num)


class Base10(Base):
    def __init__(self, num="0"):
        Base.__init__(self,"0123456789", num)


class Base16(Base):
    def __init__(self, num="0"):
        Base.__init__(self,"0123456789ABCDEF", num)


class Base64(Base):
    def __init__(self, num="0"):
        Base.__init__(self,"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", num)
        self._casing = True