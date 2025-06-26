from random import random, randint, choice
from math import log2

class Population:
    def __init__(self, size, genes, key_length, ngrams, mutation_rates, perseverance, decryption_function, gene_repetition=False):
        self.generation = 0

        self.size = size
        self.key_length = key_length
        self.genes = genes
        self.ngrams = ngrams

        # mutation_rates = (swap_rate, insertion_rate)
        self.mutation_rates = mutation_rates

        # Perseverance is the number of generations where no improvement is made until the simulation quits
        self.perseverance = perseverance
        self.last_improvement = 0
        self.decryption_function = decryption_function
        self.gene_repetition = gene_repetition

        self.keys = [self.generate_key() for key in range(size)]
        self.fitnesses = [None] * size

    def generate_key(self):
        if self.gene_repetition == False:
            key = self.genes.copy()

            # Fisher-Yates shuffle
            n = len(key)  # 26
            for i in range(n - 1, 0, -1):
                j = randint(0, i)
                key[i], key[j] = key[j], key[i]
        else:
            key = []

            for i in range(self.key_length):
                key.append(choice(self.genes))

        return key

    def calculate_fitnesses(self, ciphertext: str):
        for index in range(self.size):
            plaintext = self.decryption_function(ciphertext, self.keys[index])
            fitness = get_fitness(plaintext, self.ngrams)
            self.fitnesses[index] = fitness
        self.best_key = self.fitnesses.index(max(self.fitnesses))

        # Output to prove that the code is still improving the key
        if max(self.fitnesses) > self.fitnesses[0]:
            print(
                f"Gen {self.generation} ({int(max(self.fitnesses))}): {self.decryption_function(ciphertext[:36], self.keys[self.fitnesses.index(max(self.fitnesses))])}...")
            self.last_improvement = self.generation

    def mutate(self):
        for index in range(1, self.size):
            # Swap mutations
            # Swap two genes in the key
            while random() < self.mutation_rates[0]:
                i, j = randint(
                    0, len(self.keys[index]) - 1), randint(0, len(self.keys[index]) - 1)
                self.keys[index][i], self.keys[index][j] = self.keys[index][j], self.keys[index][i]

            # Insertion mutation
            # Move a gene to another position, and shift the other genes up or down
            while random() < self.mutation_rates[1]:
                i, j = randint(
                    0, len(self.keys[index]) - 1), randint(0, len(self.keys[index]) - 1)
                self.keys[index].insert(j, self.keys[index].pop(i))

    def evolve(self):
        self.fitnesses[0] *= 5
        total = sum(self.fitnesses)
        babies = [self.keys[self.best_key]]
        for baby in range(self.size - 1):
            parents = []
            for parent in range(2):
                num = random() * total
                index = -1
                while num >= 0:
                    index += 1
                    num -= self.fitnesses[index]
                parents.append(self.keys[index])
            babies.append(self.breed_keys(parents[0], parents[1]))
        for baby in range(len(babies)):
            self.keys[baby] = babies[baby].copy()

    def breed_keys(self, key1, key2):
        child_key = [None] * self.key_length
        for index in range(self.key_length):
            if key1[index] == key2[index]:
                child_key[index] = key1[index]
            elif not key1[index] in child_key:
                child_key[index] = key1[index]
            else:
                child_key[index] = key2[index]
        return child_key

    def simulate(self, ciphertext: str):
        while self.generation - self.last_improvement < self.perseverance:
            self.calculate_fitnesses(ciphertext)
            self.evolve()
            self.mutate()
            self.generation += 1
        self.calculate_fitnesses(ciphertext)
        key_index = self.fitnesses.index(max(self.fitnesses))
        key = self.keys[key_index]
        return key


def get_ciphertext():
    with open("input.txt", "rt") as input_file:
        input_text = input_file.read().upper()
    return input_text

def get_plaintext():
    with open("output.txt", "rt") as output_file:
        output_text = output_file.read().upper()
    return output_text

def write_plaintext(plaintext: str):
    with open("/home/elliot/OneDrive/Programming/CipherChallenge/output.txt", "wt") as output_file:
        output_file.write(plaintext)


def remove_punctuation(text: str):
    filtered_text = ""
    for char in text:
        ascii_code = ord(char.upper())
        if ascii_code > 64 and ascii_code <= 64 + 26:
            filtered_text += char.upper()
    return filtered_text


def remove_whitespace(text: str):
    filtered_text = ""
    for char in text:
        if char != ' ' and char != '\n':
            filtered_text += char.upper()
    return filtered_text


def calculate_ngram_frequencies(ns: int):
    with open(SAMPLE, "rt") as sample:
        sample_text = remove_punctuation(sample.read())
        sample_length = len(sample_text)

    ngram_count = {}
    for n in range(1, ns+1):
        ngram_count[n] = {}
        for index in range(0, len(sample_text) - (n - 1)):
            ngram = sample_text[index:index+n]
            if ngram in ngram_count[n].keys():
                ngram_count[n][ngram] += 1
            else:
                ngram_count[n][ngram] = 1

    # Convert to frequencies and write to file
    with open("/home/elliot/OneDrive/Programming/CipherChallenge/data/NgramFrequencies.txt", "wt") as ngram_frequencies:
        for n in range(1, ns+1):
            for ngram, count in ngram_count[n].items():
                frequency = round(count / sample_length, 4)
                if frequency > 0.001:
                    ngram_frequencies.write(
                        f"{ngram}:{count/len(sample_text)}\n")


def get_ngram_frequencies(ns):
    frequencies = {}
    with open("/home/elliot/OneDrive/Programming/CipherChallenge/data/NgramFrequencies.txt") as ngram_frequencies:
        lines = ngram_frequencies.readlines()
    for line in lines:
        ngram, frequency = line.split(":")
        if len(ngram) in ns:
            frequencies[ngram] = float(frequency)
    return frequencies

# def get_fitness(text: str, frequencies: dict):
#     fitness = 0
#     for string in frequencies.keys():
#         fitness += chi_squared(text, string, frequencies)
#     return 1 / fitness


def chi_squared(text: str, string: str, frequencies: dict):
    # Format for weights = [mono, di, tri] -grams
    weights = [1,1,1,1]
    observed_frequency = text.count(string) / len(text)
    expected_frequency = frequencies[string]
    return ((observed_frequency - expected_frequency) ** 2) / weights[len(string) - 1]

# def get_fitness(text: str, frequencies: dict):
#     fitness = 0
#     for string in frequencies.keys():
#         fitness += chi_squared(text, string, frequencies)
#     return 1 / fitness


def get_fitness(text: str, ns: list):
    fitness = 0
    for ngram in ENGLISH_NGRAMS:
        # print(ngram)
        # print(ns)
        if len(ngram) in ns:
            fitness += chi_squared(text, ngram, ENGLISH_FREQUENCIES)

    return 1/fitness


def index_of_coincedence(text, n=1):
    characters = set()
    for i in range(0, len(text), n):
        characters.add(text[i:i+n])

    sum = 0
    for char in characters:
        sum += text.count(char) * (text.count(char) - 1)
    index = sum / (len(text) * (len(text)-1)) * len(characters)

    return round(index, 5)


def prioritise_words():
    # This function writes all of the words in the sample text to another file, in order of "priority"
    # The priority is calculated using the word's frequency and the words length
    # Longer and more frequent words are higher priority when adding spaces back into text
    count = {}
    priorities = {}

    words = ""
    with open("data/sample.txt") as sample:
        lines = sample.read().split("\n")[:-1]

        for line in lines:
            for char in line:
                if ord(char.upper()) >= 65 and ord(char.upper()) < 65+26 or char == " ":
                    words += char.upper()
                elif char != "'":
                    words += " "

    words = words.split(" ")
    print(words)
    for word in words:
        count[word] = count.get(word, 0) + 1

    for word in count.keys():
        length_score = pow(3, len(word))
        # count_score = (count[word])
        # priorities[word] = length_score * count_score
        priorities[word] = length_score

    output = sorted(priorities)
    output = [word for word, score in sorted(
        priorities.items(), reverse=True, key=lambda item: item[1])]

    with open(DICTIONARY, "wt") as dictionary:
        for word in output:
            dictionary.write(word + "\n")


SAMPLE = "/home/elliot/OneDrive/Programming/CipherChallenge/data/sample.txt"
DICTIONARY = "data/dictionary.txt"
calculate_ngram_frequencies(4)
EXPECTED_IOC = index_of_coincedence(remove_punctuation(open(SAMPLE).read()))
ENGLISH_FREQUENCIES = get_ngram_frequencies((1, 2, 3, 4))
ENGLISH_NGRAMS = ENGLISH_FREQUENCIES.keys()
# prioritise_words()
