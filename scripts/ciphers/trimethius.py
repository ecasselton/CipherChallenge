import viginere
import cipherchallenge as cc

ciphertext = cc.remove_whitespace(cc.get_ciphertext())
key = [i for i in range(26, -1, -1)]
# key = [i for i in range(26)]
# print(len(key))
plaintext = viginere.decipher(ciphertext, key)
new_plaintext = plaintext
for char in plaintext:
    new_plaintext += chr(65+25-(ord(char)-65))
    print(char)
    print(chr(65+25-(ord(char)-65)))
cc.write_plaintext(new_plaintext)
print(new_plaintext)
