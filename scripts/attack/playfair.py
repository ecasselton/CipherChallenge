import cipherchallenge as cc

square = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'K',
    'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]

# square = [
#     'P', 'L', 'A', 'Y', 'F',
#     'I', 'R', 'E', 'X', 'M', 
#     'B', 'C', 'D', 'G', 'H',
#     'K', 'N', 'O', 'Q', 'S', 
#     'T', 'U', 'V', 'W', 'Z'
# ]

def decipher(ciphertext, square):
    plaintext = ""
    for index in range(0, len(ciphertext), 2):
        bigram = ciphertext[index:index+2]
        poses = [square.index(bigram[0]), square.index(bigram[1])]
        rows = [poses[0] //5, poses[1] //5]
        cols = [poses[0] % 5, poses[1] % 5]
        if rows[0] == rows[1]:
            cols[0] = (cols[0] - 1) % 5
            cols[1] = (cols[1] - 1) % 5
            poses = [rows[0] * 5 + cols[0], rows[1] * 5 + cols[1]]
            plaintext += square[poses[0]] + square[poses[1]]
        elif cols[0] == cols[1]:
            rows[0] = (rows[0] - 1) % 5
            rows[1] = (rows[1] - 1) % 5
            poses = [rows[0] * 5 + cols[0], rows[1] * 5 + cols[1]]
            plaintext += square[poses[0]] + square[poses[1]]
        else:
            poses = [rows[0] * 5 + cols[1], rows[1] * 5 + cols[0]]
            plaintext += square[poses[0]] + square[poses[1]]
    return plaintext

def encipher(ciphertext, square):
    plaintext = ""
    for index in range(0, len(ciphertext), 2):
        bigram = ciphertext[index:index+2]
        poses = [square.index(bigram[0]), square.index(bigram[1])]
        rows = [poses[0] //5, poses[1] //5]
        cols = [poses[0] % 5, poses[1] % 5]
        if rows[0] == rows[1]:
            cols[0] = (cols[0] + 1) % 5
            cols[1] = (cols[1] + 1) % 5
            poses = [rows[0] * 5 + cols[0], rows[1] * 5 + cols[1]]
            plaintext += square[poses[0]] + square[poses[1]]
        elif cols[0] == cols[1]:
            rows[0] = (rows[0] + 1) % 5
            rows[1] = (rows[1] + 1) % 5
            poses = [rows[0] * 5 + cols[0], rows[1] * 5 + rows[1]]
            plaintext += square[poses[0]] + square[poses[1]]
        else:
            poses = [rows[0] * 5 + cols[1], rows[1] * 5 + cols[0]]
            plaintext += square[poses[0]] + square[poses[1]]
    return plaintext

def get_key(ciphertext: str):
    population = cc.Population(SIZE, GENES, len(GENES), NGRAMS, MUTATION_RATES, PERSEVERANCE, decipher)

    key = population.simulate(ciphertext)
    return key

SIZE = 500
GENES = square
NGRAMS = (2,3)
MUTATION_RATES = (0.5, 0.0)
PERSEVERANCE = 400

ciphertext = cc.remove_punctuation(cc.get_ciphertext())
# print(encipher(ciphertext, square))
key = get_key(ciphertext)
plaintext = decipher(ciphertext, key)

print(plaintext)
print(key)
