import cipherchallenge as cc
import numpy as np
from random import randint

ciphertext = cc.get_ciphertext()

def encrypt(plaintext, key_matrix, n):
    ciphertext = ""
    for i in range(0, len(plaintext), n):
        block = np.array([ord(char)-65 for char in plaintext[i:i+n]])
        product = np.matmul(key_matrix, block)
        for k in product:
            ciphertext += chr(k % 27 + 65)
    return ciphertext

        
n = 2
# key = np.zeros((3,3), np.int64)
# for i in range(3):
#     for j in range(3):
#         key[i,j] = randint(0, 26)

# key = np.array([[13, 2], [2, 8], [6, 19]])
# inv = np.array([[22, 21, 13], [11, 8, 14], [4, 13, 14]])
# print(np.matmul(key, inv))
# print(key)

key = np.zeros((n, n), np.int64)
for i in range(n):
    for j in range(n):
        key[i,j] = randint(0, 26)


print(key)

ciphertext = encrypt(cc.remove_punctuation(cc.get_ciphertext()),key,n)
print(ciphertext)
# cc.write_plaintext(ciphertext)
# print(encrypt(ciphertext,inv,3))
