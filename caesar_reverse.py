#!/usr/bin/python3

from classes.CAESAR import CAESAR
from sys import stdin

'''
    Reads a CAESAR cipher from the stdin and bruteforces it against the default alphabeth
'''

caesar = CAESAR()

cipher = ""

for line in stdin:
  cipher += line

caesar.setCipher(cipher)
caesar.setKey(13)



for key in  range(len(caesar.getAlphabeth())):
    caesar.setKey(key)
    caesar.decrypt()
    print(f"{key}: {caesar.getText()}")