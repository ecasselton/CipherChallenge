# Uses a large population
import cipherchallenge as cc 

def decipher(ciphertext, key):
    deciphered_text = str()
    for letter in ciphertext:
        if letter in key:
            deciphered_text += chr(key.index(letter) + 65)
        else:
            deciphered_text += letter
    return deciphered_text

def get_key(ciphertext: str):
    population = cc.Population(SIZE, GENES, len(GENES), NGRAMS, MUTATION_RATES, PERSEVERANCE, decipher)

    key = population.simulate(ciphertext)
    return key

SIZE = 400
GENES = [chr(ascii) for ascii in range(65, 65+26, 1)]
NGRAMS = (1, 2, 3)
MUTATION_RATES = (0.4, 0)
PERSEVERANCE = 100

ciphertext = cc.get_ciphertext()
key = get_key(cc.remove_punctuation(ciphertext))
plaintext = decipher(ciphertext, key)
print()
print(plaintext)
print()
print("KEY: ", end="")
for letter in key:
    print(letter, end='')
print()
cc.write_plaintext(plaintext)
