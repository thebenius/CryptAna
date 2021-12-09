#!/usr/bin/python3

from tools.Base import *

num1 = Base16()
num2 = Base64("LrfAN")

num1.setInt(num2.getInt())

print(num1)