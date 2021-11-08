#!/usr/bin/python3

from classes.CAESAR import CAESAR
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


caesar = CAESAR()
text = ""
key = 0

if (mode == 'r'):
  print("Cipher:")

else:
  print("key: ", end='')
  key = int(input())

  if (mode == 'e'):
    print("Plaintext:")
  if (mode == 'd'):
    print("Cipher")


for line in stdin:
  text += line

if (mode == 'r'):
  caesar.setCipher(text)
  print("\n\nPossible Solutions:")
  for key in  range(len(caesar.getAlphabeth())):
      caesar.setKey(key)
      print(f"{key}: {caesar.decrypt()}")
  exit()

caesar.setKey(key)

if (mode == 'e'):
  caesar.setText(text)
  print(caesar.encrypt())
  
if (mode == 'd'):
  caesar.setCipher(text)
  print(caesar.decrypt())




