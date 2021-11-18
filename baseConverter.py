#!/usr/bin/python3

from classes.Base import *

num1 = Base16()
num2 = Base64("LrfAN")

num1.setDecimal(num2.getDecimal())

print(num1)