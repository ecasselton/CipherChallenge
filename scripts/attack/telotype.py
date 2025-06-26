import cipherchallenge as cc
from random import randint, random
import math

symbols = "|\\/"

class SimulatedAnnealing:
    def __init__(self, max_steps, decryption_function):
        self.key = self.random_key()
        self.max_steps = max_steps
        self.decryption_function = decryption_function
        self.num_chars = 27

        self.fitness = 0
        self.step = 0

    def random_key(self):
        key = []
        for i in range(7):
            swap = [randint(0, 1), randint(0, 1), randint(0, 1)]
            key.append(swap)
        return key

    def next_step(self, ciphertext: str):
        new_key = self.mutate(self.key)
        plaintext = self.decryption_function(ciphertext, new_key)
        # fitness = cc.index_of_coincedence(plaintext)
        fitness = cc.get_fitness(plaintext, NGRAMS)
        temperature = 1 / (self.step + 1) ** 0.5
        # temperature = math.exp(-0.001 * self.step)
        chars = set()

        probability = self.acceptance_probability(fitness, temperature)
        if probability > random():
            if fitness > self.fitness:
                print(f"Step {self.step} ({int(fitness)}): {self.decryption_function(ciphertext, self.key)[:100]}...")
            for char in plaintext:
                chars.add(char)
            self.num_chars = len(chars)
            self.fitness = fitness
            self.key = new_key.copy()
            # Output to prove that the code is still improving the key
    
    def acceptance_probability(self, new_fitness, temperature):
        if new_fitness > self.fitness:
            return 1
        else:
            # print((self.fitness-new_fitness) / temperature)
            return math.exp((new_fitness - self.fitness) / temperature)

    def mutate(self, key):
        # Swap two genes in the key
        new_key = key.copy()
        # while random() <= self.mutation_rate:
        i, j = randint(0, 6), randint(0, 2)
        new_key[i][j] = randint(0, 1)
        return new_key

    def simulate(self, ciphertext: str):
        while self.step < self.max_steps:
            self.next_step(ciphertext)
            self.step += 1
        return self.key

def decipher(ciphertext, key):
    blocks = []
    key_index = 0
    for j in range(0, len(ciphertext), 3):
        blocks.append("")
        trigram = [sym for sym in ciphertext[j:j+3]]
        swaps = key[key_index]
        for i in range(3):
            if swaps[i] and trigram[i] != '|':
                trigram[i] = '/' if trigram[i] == '\\' else '\\'
            blocks[j//3] += trigram[i]
        key_index = (key_index + 1) % len(key)

    # Convert from \|/
    plaintext = ""
    for block in blocks:
        num = 0
        for i in range(3):
            num += symbols.index(block[i]) * 3**(2-i)

        char = chr((num+10)%27+65)
        plaintext += char
    
    return plaintext

NGRAMS = (1,2,3,4)
period = 7
ciphertext = cc.remove_whitespace(cc.get_ciphertext())

# ciphertext = telo.encipher(ciphertext, [(0,0,1) for i in range(period)])

attack = SimulatedAnnealing(10000, decipher)
key = attack.simulate(ciphertext)

print(decipher(ciphertext, key))
