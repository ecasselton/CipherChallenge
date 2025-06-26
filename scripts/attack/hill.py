import cipherchallenge as cc
import numpy as np
from random import randint, random, choice

class SimulatedAnnealing:
    def __init__(self, example_key, max_steps, decryption_function):
        # self.key = self.random_key()
        self.key = example_key
        self.max_steps = max_steps
        self.decryption_function = decryption_function

        self.fitness = 0
        self.step = 0

    def random_key(self):
        key = np.zeros((N, N), np.int64)
        for i in range(N):
            for j in range(N):
                key[i,j] = randint(0, 26)
        return key

    def next_step(self, ciphertext: str):
        new_key = self.mutate(self.key)
        plaintext = self.decryption_function(ciphertext, new_key)
        fitness = cc.get_fitness(plaintext, (1,2,3,4))
        temperature = 1 / (self.step + 1) ** 0.01
        print(new_key)
        print(self.fitness)
        print(fitness)
        input()

        probability = self.acceptance_probability(fitness, temperature)
        if probability > random():
            print(f"Step {self.step} ({int(self.fitness)}): {self.decryption_function(ciphertext, self.key)[:120]}...")
            self.fitness = fitness
            self.key = new_key.copy()
            # Output to prove that the code is still improving the key
    
    def acceptance_probability(self, new_fitness, temperature):
        if new_fitness > self.fitness:
            return 1
        else:
            # print((self.fitness-new_fitness) / temperature)
            return np.exp((new_fitness - self.fitness) / temperature)

    def mutate(self, key):
        new_key = key.copy()
        i, j = randint(0, N-1), randint(0, N-1)
        new_key[i,j] = (new_key[i,j] + choice((-2, -1, 1, 2))) % 27
        return new_key

    def simulate(self, ciphertext: str):
        while self.step <= self.max_steps:
            self.next_step(ciphertext)
            self.step += 1
        return self.key

ciphertext = cc.get_ciphertext()

def decrypt(ciphertext, inverse_key, n):
    plaintext = ""
    for i in range(0, len(ciphertext), n):
        # print(ciphertext[])
        block = np.array([ord(char)-65 for char in ciphertext[i:i+n]])
        # print(block)
        product = np.matmul(inverse_key, block)
        for k in product:
            plaintext += chr(k % 27 + 65)
    return plaintext

        
ciphertext = cc.remove_whitespace(cc.get_ciphertext())
NUM_STEPS = 100000
N = 2
DECRYPTION_FUNCTION = lambda ciphertext, key: decrypt(ciphertext, key, N)
EXAMPLE_KEY = np.array([[7, 26], [8, 11]])

attack = SimulatedAnnealing(EXAMPLE_KEY, NUM_STEPS, DECRYPTION_FUNCTION)
keys = attack.simulate(ciphertext)
print(keys)
