# Beaufort cipher is almost identical to the viginere cipher, and can be solved
# as such if each letter in the alphabet is switched with its 'inverse'
# A -> Z, B -> Y ...

import cipherchallenge as cc
import viginere

ciphertext = cc.get_ciphertext()
inversed_ciphertext = ""

for char in cc.remove_punctuation(ciphertext):
    inversed_ciphertext += chr(65 + 25 - (ord(char) - 65))

period = viginere.get_period(inversed_ciphertext)
key = viginere.get_key(inversed_ciphertext, period)
plaintext = viginere.decipher(inversed_ciphertext, key)

print(plaintext)
for shift in key:
    print(chr(25 - shift + 65), end="")
print()

cc.write_plaintext(plaintext)
