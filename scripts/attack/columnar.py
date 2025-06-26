import cipherchallenge as cc

def get_factors(ciphertext_length):
    factors = []
    for num in range(2, 10):
        if ciphertext_length % num == 0:
            factors.append(num)
    return sorted(factors)

def decipher(ciphertext, permutation, read=0, write=0):
    # Modes (described as the process of encryption):
    # 0 - Across
    # 1 - Down

    width = len(permutation)
    height = len(ciphertext) // width
    cells = [[""] * width for col in range(height)]
    plaintext = ""
    if read == 0:
        for row in range(height):
            for col in range(width):
                cells[row][col] = ciphertext[row * width + permutation.index(col)]
    elif read == 1:
        for col in range(width):
            for row in range(height):
                cells[row][col] = ciphertext[row + height * permutation.index(col)]
    if write == 0:
        for row in range(height):
            for col in range(width):
                plaintext += cells[row][col]

    return plaintext

def get_permutation(ciphertext):
    factors = get_factors(len(ciphertext))
    # factors = [6]
    print(f"Factors are {factors}")
    permutations = []

    for factor in factors:
        print(f"====== Factor {factor} ======")
        size = factor ** 2
        perseverance = 20
        genes = list(range(0, factor))
        mutation_rates = (0.9, 0.9)
        population = cc.Population(size, genes, factor, NGRAMS, mutation_rates, perseverance, decipher)

        perm = population.simulate(ciphertext)
        permutations.append(perm)
    
    best_fitness = 0
    best_perm = []
    for perm in permutations:
        plaintext = decipher(ciphertext, perm)
        fitness = cc.get_fitness(plaintext, range(3))
        if fitness > best_fitness:
            best_fitness = fitness
            best_perm = perm
    
    return best_perm

if __name__ == "__main__":
    NGRAMS = (2, 3)
    
    FREQS = cc.get_ngram_frequencies((2, 3))
    
    ciphertext = cc.remove_punctuation(cc.get_ciphertext())
    
    permutation = get_permutation(ciphertext)
    plaintext = decipher(ciphertext, permutation);
    
    print()
    print(plaintext)
    print()
    print(f"PERMUTATION: {permutation}")
    cc.write_plaintext(plaintext);
