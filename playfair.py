#!/usr/bin/python3

from ciphers.PLAYFAIR import PLAYFAIR
from tools.Analyser import Analyser
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


playfair = PLAYFAIR()
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
    print("Cipher:")


for line in stdin:
  if (line == '\n'):
    break
  else:
    text += line


'''
  this mode is not supported yet. and highly experimental
'''
if (mode == 'r'):
    playfair.setCipher(text)
    analyzer = Analyser()
    analyzer.setText(playfair.getCipher())
    print(analyzer.getLetters(2))
    


    

playfair.setKey(key)

if (mode == 'e'):
  playfair.setText(text)
  print(playfair.encrypt())

if (mode == 'd'):
  playfair.setCipher(text)
  print(playfair.decrypt())





