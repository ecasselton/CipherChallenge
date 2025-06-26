import cipherchallenge as cc
import math
from random import randint, choice, random

class HillClimbingAttack:
    def __init__(self, genes, mutation_rates, perseverance, decryption_function, ngrams, stability):
        self.genes = genes
        self.mutation_rates = mutation_rates
        self.perseverance = perseverance
        self.decryption_function = decryption_function
        self.ngrams = ngrams
        self.stability = stability

        self.parent_key = self.generate_key(self.genes)
        self.child_key = self.parent_key.copy()
        self.fitness = 0
        self.generation = 0
        self.last_improvement = 0

    def generate_key(self, genes):
        key = self.genes

        # Fisher-Yates shuffle
        n = len(key) #26
        for i in range(n - 1, 0, -1):
            j = randint(0, i)
            key[i], key[j] = key[j], key[i]

        return key

    def update_parent(self, ciphertext: str):
        plaintext = self.decryption_function(ciphertext, self.child_key)
        fitness = cc.get_fitness(plaintext, self.ngrams)

        if fitness > self.fitness or random() < 1 / (self.fitness ** self.stability * (self.fitness-fitness-1) ** 2):
            self.fitness = fitness
            self.parent_key = self.child_key.copy()
            # Output to prove that the code is still improving the key
            print(f"Gen {1 + self.generation} ({int(self.fitness)}): {self.decryption_function(ciphertext[:64], self.parent_key)}...")
            self.last_improvement = self.generation

    def mutate(self):
        # Swap two genes in the key
        self.child_key = self.parent_key.copy()
        if random() <= self.mutation_rates[0]:#self.mutation_rates[0] * math.e ** -(self.generation / 1000):
            i, j = randint(0, len(self.child_key) - 1), randint(0, len(self.child_key) - 1)
            self.child_key[i], self.child_key[j] = self.child_key[j], self.child_key[i]

        # Move a gene to another position, and shift the other genes up or down
        # while random() <= self.mutation_rates[1]:
        #     i, j = randint(0, len(self.child_key) - 1), randint(0, len(self.child_key) - 1)
        #     self.child_key.insert(j, self.child_key.pop(i))

    def simulate(self, ciphertext: str):
        while self.generation - self.last_improvement < self.perseverance:
            self.mutate()
            self.update_parent(ciphertext)
            self.generation += 1

def decipher(ciphertext, key):
    deciphered_text = str()
    for letter in ciphertext:
        if letter in key:
            deciphered_text += chr(key.index(letter) + 65)
        else:
            deciphered_text += letter
    return deciphered_text

genes = [chr(ascii) for ascii in range(65, 65+26)]
MUTATION_RATES = (0.4, 0.0)
PERSEVERANCE = 10000
STABILITY = 3
NGRAMS = (1,2,3,4)

ciphertext = cc.remove_punctuation(cc.get_ciphertext())
attack = HillClimbingAttack(genes, MUTATION_RATES, PERSEVERANCE, decipher, NGRAMS, STABILITY)
attack.simulate(ciphertext)
print("".join(attack.parent_key))

cc.write_plaintext(decipher(ciphertext, attack.parent_key))
