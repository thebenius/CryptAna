#!/usr/bin/python3
from tools.Base import *
from ciphers.FIXEDXOR import FIXEDXOR

num1 = Base16("1c0111001f010100061a024b53535009181c")
num2 = Base16("686974207468652062756c6c277320657965")

fixedxor = FIXEDXOR()
fixedxor.setText(num1)
fixedxor.setKey(num2)

num3 = Base16()
num3.setInt(fixedxor.encrypt())

print(num3)