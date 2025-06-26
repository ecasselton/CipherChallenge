import cipherchallenge as cc
from random import random, randint, choice
from itertools import combinations

class HillClimbingAttack:
    def __init__(self, genes, mutation_rates, perseverance, decryption_function, ngrams, stability):
        self.genes = genes
        self.mutation_rates = mutation_rates
        self.perseverance = perseverance
        self.decryption_function = decryption_function
        self.ngrams = ngrams
        self.stability = stability

        self.parent_key = []#self.generate_key(self.genes)
        self.child_key = []#self.parent_key.copy()
        self.fitness = 0
        self.generation = 0
        self.last_improvement = 0
        self.maximum_found = False

    def generate_key(self, genes):
        key = []
        for i in range(2):
            square = self.genes.copy()

            # Fisher-Yates shuffle
            n = 25
            for i in range(n - 1, 0, -1):
                j = randint(0, i)
                square[i], square[j] = square[j], square[i]
            key.append(square)

        # key.append(self.genes.copy())
        # key.append(self.genes.copy())
        return key

    # def find_best(self):
    #     child_key = [[], [], [], []]
    #     best_fitness = 0
    #     best_key = [[], [], [], []]
    #     for square in range(1, 3, 1):
    #         for a in range(25):
    #             for b in range(a, 25-a):
    #                 for i in range(len(self.parent_key)):
    #                     child_key[i] = self.parent_key[i].copy()
    #                 child_key[square][a], child_key[square][b] = child_key[square][b], child_key[square][a]
    #                 fitness = cc.get_fitness(self.decryption_function(ciphertext, child_key), self.frequencies)
    #                 if fitness > best_fitness:
    #                     best_fitness = fitness
    #                     for i in range(4):
    #                         best_key[i] = child_key[i].copy()
    #     for i in range(4):
    #         self.child_key[i] = best_key[i].copy()
    #     #self.child_key = best_key.copy()


    def update_parent(self, ciphertext: str):
        plaintext = self.decryption_function(ciphertext, self.child_key)
        fitness = cc.get_fitness(plaintext, self.ngrams)
        if fitness > self.fitness:# or random() < 1 / self.fitness ** self.stability * abs((self.fitness-fitness-1) ** 1):
            for i in range(len(self.child_key)):
                self.parent_key[i] = self.child_key[i].copy()
            # Output to prove that the code is still improving the key
            print(f"Gen {1 + self.generation} ({round(self.fitness, 6)}): {self.decryption_function(ciphertext[:72], self.parent_key)}...")
            self.last_improvement = self.generation
            self.fitness = fitness

        elif random() < 0.003:# / (self.fitness ** self.stability * (self.fitness - fitness - 1) ** 2):
            for i in range(len(self.child_key)):
                self.parent_key[i] = self.child_key[i].copy()
            self.fitness = fitness
            #else:
        #    self.maximum_found = True

    def mutate(self):
        for i in range(len(self.parent_key)):
            self.child_key[i] = self.parent_key[i].copy()
        # Swap two genes in the key
        square = randint(0, 1)
        i, j = randint(0, len(self.child_key[square]) - 1), randint(0, len(self.child_key[square]) - 1)
        self.child_key[square][i], self.child_key[square][j] = self.child_key[square][j], self.child_key[square][i]


        # Move a gene to another position, and shift the other genes up or down
        # while random() <= self.mutation_rates[1]:
        #     i, j = randint(0, len(self.child_key) - 1), randint(0, len(self.child_key) - 1)
        #     self.child_key.insert(j, self.child_key.pop(i))

    def simulate(self, ciphertext: str):
        # best_fitness = 0
        # global_key = [[], [], [], []]
        # while True:
        self.parent_key = self.generate_key(self.genes)
        print(self.parent_key)
        self.child_key = self.parent_key.copy()
        # self.fitness = 0
        # self.generation = 0
        # self.last_improvement = 0
        # best_key = [[], [], [], []]
        # while not self.maximum_found:
        # while self.generation - self.last_improvement < self.perseverance:
        while True:
            self.mutate()
            # self.find_best()
            self.update_parent(ciphertext)
            self.generation += 1
            if self.fitness > 1200:
                with open("outputkey.txt", "wt") as file:
                    for square in key:
                        for row in range(5):
                            for col in range(5):
                                file.write(square[row * 5 + col], end=" ")
                            file.write("\n")
                        file.write("\n")
            # if self.fitness > best_fitness:
            #     best_fitness = self.fitness
            #     for i in range(len(self.parent_key)):
            #         self.parent_key[i] = self.child_key[i].copy()
                        
            # Output to prove that the code is still improving the key
            # print(f"Gen {1 + self.generation} ({int(self.fitness)}): {self.decryption_function(ciphertext[:36], self.parent_key)}...")
        # print("Maximum found, restarting...")
        # self.maximum_found = False
        # if self.parent_key > 1000:
        #     for square in best_key:
        #         for row in range(5):
        #             for col in range(5):
        #                 print(square[row * 5 + col], end=" ")
        #             print()
        #         print()
        #     input("Continue? ")
        #     global_fitness = self.fitness
        #     for i in range(len(self.parent_key)):
        #         best_key[i] = self.parent_key[i].copy()
        # self.parent_key = best_key

def decipher(ciphertext, key, period):
    shuffled = ""
    square1, square2 = key
    # bigrams = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    for index in range(0, len(ciphertext), 2):
        bigram = ciphertext[index:index+2]

        for i in range(2):
            coord1 = [square2.index(bigram[0]) // 5, square2.index(bigram[0]) % 5]
            coord2 = [square1.index(bigram[1]) // 5, square1.index(bigram[1]) % 5]
            bigram = ""
            # Same row
            if coord1[0] == coord2[0]:
                coord1[1] = (coord1[1] + 1) % 5
                coord2[1] = (coord2[1] + 1) % 5
                bigram += square1[coord2[0] * 5 + coord2[1]]
                bigram += square2[coord1[0] * 5 + coord1[1]]
            else:
                coord1[1], coord2[1] = coord2[1], coord1[1]
                bigram += square1[coord1[0] * 5 + coord1[1]]
                bigram += square2[coord2[0] * 5 + coord2[1]]
        shuffled += bigram

    plaintext = ""
    blocks = [shuffled[i:i+period*2] for i in range(0, len(shuffled), period*2)]

    for block in blocks:
        for i in range(2):
            for j in range(int(len(block)/2)):
                plaintext += block[i+j*2]

    return plaintext

GENES = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'K',
    'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]

def get_key(ciphertext: str):
    attack = HillClimbingAttack(GENES, MUTATION_RATES, PERSEVERANCE, DECRYPTION_FUNCTION, NGRAMS, STABILITY)

    attack.simulate(ciphertext)
    return attack.parent_key

NGRAMS = (1,2,3)
MUTATION_RATES = (1, 0.0)
PERSEVERANCE = 20000
STABILITY = 0.5
DECRYPTION_FUNCTION = lambda ciphertext, key : decipher(ciphertext, key, 7)

# square1 = [char for char in "POLYBIUSACDEFGHKMNQRTVWXZ"]
# square2 = [char for char in "KRFMTEDGNUYAHPVWBIQXOCLSZ"]
# key = (square1, square2)

# ciphertext = "TWFAATNIOYRAXMTAMZAOMRIVASEAPRIGAAFQAK"
# print(decipher(ciphertext, key, 7))

ciphertext = cc.remove_whitespace(cc.get_ciphertext())
# print(encipher(ciphertext, [GENES.copy() for i in range(4)]))
key = get_key(ciphertext)
print(key)
# plaintext = decipher(ciphertext, key)
#
# for square in key:
#     for row in range(5):
#         for col in range(5):
#             print(square[row * 5 + col], end=" ")
#         print()
#     print()
# print(plaintext)
