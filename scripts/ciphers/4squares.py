import cipherchallenge as cc
from random import random, randint, choice

squares = [
    [
        'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'K',
        'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z'
    ],
    [
        'M', 'A', 'I', 'S', 'E',
        'F', 'G', 'H', 'K', 'L',
        'N', 'O', 'P', 'Q', 'R',
        'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', 'B', 'C', 'D'
    ],
    [
        'S', 'T', 'A', 'N', 'L',
        'E', 'Y', 'Z', 'B', 'C',
        'D', 'F', 'G', 'H', 'I',
        'K', 'M', 'O', 'P', 'Q',
        'R', 'U', 'V', 'W', 'X'
    ],
    [
        'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'K',
        'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z'
    ]
]

def decipher(ciphertext, squares):
    plaintext = ""
    # bigrams = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    for index in range(0, len(ciphertext), 2):
        bigram = ciphertext[index:index+2]
        poses = [squares[1].index(bigram[0]), squares[2].index(bigram[1])]
        rows = [poses[0] //5, poses[1] //5]
        cols = [poses[0] % 5, poses[1] % 5]
        plaintext += squares[0][rows[0] * 5 + cols[1]]
        plaintext += squares[3][rows[1] * 5 + cols[0]]
    
    return plaintext

def encipher(ciphertext, squares):
    plaintext = ""
    # bigrams = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    for index in range(0, len(ciphertext), 2):
        bigram = ciphertext[index:index+2]
        poses = [squares[0].index(bigram[0]), squares[3].index(bigram[1])]
        rows = [poses[0] //5, poses[1] //5]
        cols = [poses[0] % 5, poses[1] % 5]
        plaintext += squares[1][rows[0] * 5 + cols[1]]
        plaintext += squares[2][rows[1] * 5 + cols[0]]
    
    return plaintext


ciphertext = cc.remove_whitespace(cc.get_ciphertext())
print(decipher(ciphertext, squares))
