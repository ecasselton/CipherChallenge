import cipherchallenge as cc
from random import randint, random

class TranspositionAttack:
    def __init__(self, example_key, perseverance, volatility):
        self.key = example_key
        self.randomise_key()
        self.perseverance = perseverance
        self.volatility = volatility

        self.fitness = 37
        self.generation = 0
        self.last_improvement = 0
        self.done = False

    def randomise_key(self):
        # Fisher-Yates shuffle
        n = len(self.key) #26
        for i in range(n - 1, 0, -1):
            j = randint(0, i)
            self.key[i], self.key[j] = self.key[j], self.key[i]

    def update_key(self, ciphertext: str):
        key = self.mutate()
        plaintext = self.permute(ciphertext, key)
        fitness = self.objective(plaintext)
        if fitness <= 26:
            self.done = True

        if fitness < self.fitness or (random() < self.volatility and not self.done):
            self.fitness = fitness
            self.key = key.copy()
            # Output to prove that the code is still improving the key
            print(f"Gen {1 + self.generation} ({int(self.fitness)}): {plaintext[:100]}")
            self.last_improvement = self.generation

    def mutate(self):
        key = self.key.copy()
        if random() < 0.5:
            i, j = randint(0, len(key) - 1), randint(0, len(key) - 1)
            key[i], key[j] = key[j], key[i]
        else:
            i, j = randint(0, len(key) - 1), randint(0, len(key) - 1)
            key.insert(j, key.pop(i))
        return key

    def simulate(self, ciphertext: str):
        while not self.done and self.generation < self.perseverance:
            self.update_key(ciphertext)
            self.generation += 1
        print(f"Key length {len(self.key)} ({int(self.fitness)}): {self.permute(ciphertext, self.key)}")

    def permute(self, ciphertext, key):
        # columns = [ciphertext[column*n : (column+1)*n] for column in key]
        rows = [ciphertext[i:i+len(key)] for i in range(0, len(ciphertext), len(key))]
        shuffled = ""
        for row in rows:
            for col in key:
                shuffled += row[col]
        return shuffled

    def objective(self, plaintext):
        # return cc.index_of_coincedence(plaintext, 2)
        return len(set([plaintext[i:i+2] for i in range(0, len(plaintext), 2)]))

factors = [3, 4, 6, 7, 8, 9]

for factor in factors:
    ciphertext = cc.remove_whitespace(cc.get_ciphertext())
    example_key = list(range(factor))
    transpositionAttack = TranspositionAttack(example_key, 100000, 0)
    transpositionAttack.simulate(ciphertext)
