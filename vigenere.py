#!/usr/bin/python3

from classes.VIGENERE import VIGENERE
from classes.Analyser import Analyser
from sys import stdin


print("Please select the mode:")
print("encrypt (e)")
print("decrypt (d)")
print("reverse (r)")
print("mode: ", end='')
mode = list(input())[0]
if (mode != 'e' and mode != 'd' and mode != 'r'):
  print("invalid mode")
  exit()


vigenere = VIGENERE()
text = ""
key = ""

if (mode == 'r'):
  print("Cipher:")

else:
  print("key: ", end='')
  key = input()

  if (mode == 'e'):
    print("Plaintext:")
  if (mode == 'd'):
    print("Cipher")


for line in stdin:
  if (line == '\n'):
    break
  else:
    text += line

if (mode == 'r'):
    analyzer = Analyser()
    analyzer.setText(text)
    print(analyzer.commonDividers())
    keylen = int(input())
    print(keylen)
    cols = [""] * keylen
    for i in range(len(text)):
        cols[i%keylen] += text[i]
    key = ""
    for col in cols:
        analyzer.setText(col)
        key += chr(ord(analyzer.getLetters()[0][0]) - 4)
    
    vigenere.setCipher(text)
    vigenere.setKey(key)
    print(vigenere.decrypt())
    print(key)


    

vigenere.setKey(key)

if (mode == 'e'):
  vigenere.setText(text)
  print(vigenere.encrypt())
  
if (mode == 'd'):
  vigenere.setCipher(text)
  print(vigenere.decrypt())




