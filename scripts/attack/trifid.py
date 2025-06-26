import cipherchallenge as cc
from random import randint, random
import math

class SimulatedAnnealing:
    def __init__(self, example_key, mutation_rate, max_steps, init_temp, decryption_function):
        self.key = example_key
        self.mutation_rate = mutation_rate
        self.max_steps = max_steps
        self.init_temp = init_temp
        self.decryption_function = decryption_function

        self.randomise_key()
        self.fitness = 0
        self.step = 0

    def randomise_key(self):
        # Fisher-Yates shuffle
        n = len(self.key)
        for i in range(n - 1, 0, -1):
            j = randint(0, i)
            self.key[i], self.key[j] = self.key[j], self.key[i]

    def next_step(self, ciphertext: str):
        new_key = self.mutate(self.key)
        plaintext = self.decryption_function(ciphertext, new_key)
        fitness = cc.get_fitness(plaintext, (1,2,3,4))
        temperature = 1 / (self.step + 1)**0.01
        # temperature = math.exp(-0.001 * self.step)

        probability = self.acceptance_probability(fitness, temperature)
        if probability > random():
            if fitness > self.fitness:
                print(f"Step {self.step} ({int(self.fitness)}): {self.decryption_function(ciphertext[:96], self.key)}...  {"".join(self.key)}")
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
        i, j = randint(0, len(new_key) - 1), randint(0, len(new_key) - 1)
        new_key[i], new_key[j] = new_key[j], new_key[i]
        return new_key

    def simulate(self, ciphertext: str):
        while self.step <= self.max_steps:
            self.next_step(ciphertext)
            self.step += 1
        return self.key


def decipher(ciphertext, period, key):
    blocks = [ciphertext[i:i+period] for i in range(0, len(ciphertext), period)]
    plaintext = ""
    for block in blocks:
        rect = [[]]
        j = 0
        for char in block:
            value = key.index(char)
            for i in (9, 3, 1):
                rect[j//len(block)].append(value // i)
                value %= i
                j += 1
                if (j % len(block) == 0):
                    rect.append([])

        for i in range(len(block)):
            plaintext += key[rect[0][i] * 9 + rect[1][i] * 3 + rect[2][i]]

    return plaintext


PERIOD = 7
NGRAMS = (1,2,3)
NUM_STEPS = 100000
DECRYPTION_FUNCTION = lambda ciphertext, key : decipher(ciphertext, PERIOD, key)
MUTATION_RATE = 0.5
VOLATILITY = 0.0003
ciphertext = cc.remove_whitespace(cc.get_ciphertext())

hill_climbing = SimulatedAnnealing([char for char in "KEYWORDABCFGHIJLMNPQSTUVXZ+"], MUTATION_RATE, NUM_STEPS, 100, DECRYPTION_FUNCTION)

key = hill_climbing.simulate(ciphertext)
print(key)
print(decipher(ciphertext, PERIOD, key))
# period = 7
# plaintext = decipher(ciphertext, period, key)
# print(plaintext)
