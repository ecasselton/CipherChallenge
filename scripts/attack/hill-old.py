import cipherchallenge as cc
import math
import numpy as np

def decipher(ciphertext, key_inverse):
    plaintext = ""
    
    for a in range(0, len(ciphertext), BLOCK_LENGTH):
        block = np.array([ord(ciphertext[i])-65 for i in range(a, a+BLOCK_LENGTH)])
        product = key_inverse.dot(block)
        for num in product:
            plaintext += chr((num % 26)+65)
    return plaintext

# def get_key_inverse():
#     population = cc.Population(SIZE, GENES, BLOCK_LENGTH ** 2, NGRAMS, MUTATION_RATES, PERSEVERANCE, decipher, True)
#
#     key_inverse = population.simulate(ciphertext)
#     
#     return key_inverse

def get_key_inverse():
    plaintext = ""
    best_fitness = 0
    best_key = [0, 0, 0, 0]
    for a in range(26):
        print(f"{a}/26")
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    matrix = np.array([[a, b], [c, d]])
                    determinant = np.linalg.det(matrix)
                    if not (determinant == 0 or determinant == 13 or determinant == 2):
                        plaintext = decipher(ciphertext, matrix)
                        fitness = cc.get_fitness(plaintext, FREQS)
                        if fitness > best_fitness:
                            best_fitness = fitness
                            best_key = matrix.copy()
    return best_key


BLOCK_LENGTH = 2
# SIZE = 100
# GENES = list(range(26))
# NGRAMS = (1, 2, 3)
# MUTATION_RATES = (0.5, 0)
# PERSEVERANCE = 200
FREQS = cc.get_ngram_frequencies((1,2,3))

ciphertext = cc.remove_punctuation(cc.get_ciphertext())

key_inverse = get_key_inverse()

for row in range(BLOCK_LENGTH):
    print('| ', end='')
    for column in range(BLOCK_LENGTH):
        print(str(key_inverse[row * BLOCK_LENGTH + column]).ljust(3, ' '), end = '')
    print('|')

print(decipher(ciphertext, key_inverse))
