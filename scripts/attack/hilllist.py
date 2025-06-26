import cipherchallenge as cc
import math

def decipher(ciphertext, key_inverse):
    plaintext = ""
    
    block_length = int(math.sqrt(len(key_inverse)))

    for a in range(0, len(ciphertext), block_length):
        block = ciphertext[a:a+block_length]
        for row in range(block_length):
            sum = 0
            for char in range(block_length):
                sum += (ord(block[char])-65) * key_inverse[row*block_length+char]
            plaintext += chr((sum % 26) + 65)
    return plaintext

# def get_key_inverse():
#     population = cc.Population(SIZE, GENES, BLOCK_LENGTH ** 2, NGRAMS, MUTATION_RATES, PERSEVERANCE, decipher, True)
#
#     key_inverse = population.simulate(ciphertext)
#     
#     return key_inverse
def det(matrix):
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]

def get_key_inverse():
    plaintext = ""
    best_fitness = 0
    best_key = [0, 0, 0, 0]
    for a in range(26):
        print(f"{a}/26")
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    matrix = [a, b, c, d]
                    determinant = det(matrix)
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
