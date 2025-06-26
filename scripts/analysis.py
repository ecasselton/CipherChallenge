import cipherchallenge as cc
import math

def draw_graph(data: list, height: int, scale: int, step: int):
    # Unpacks the data from a list of tuples
    labels = []
    values = []
    for index in range(len(data)):
        labels.append(data[index][0])
        values.append(data[index][1])

    # Draws a bar chart of the data
    # maximum = max(values)
    for row in range(height, 0, -scale):
        if row % step == 0:
            print(f"{str(row).ljust(3)}-", end="")
        else:
            print("    ", end="")
        for val in values:
            if val >= row:
                print("  ▉ ", end="")
            else:
                print("    ", end="")
            # print(" " * spacing)
        print()
    print("    ", end="")
    for label in labels:
        print(f" {str(label).rjust(2)} ", end="")

def frequency(ciphertext, ngram):
    ngrams = set()
    frequencies = []

    # Creates a list of the ngrams in the ciphertext
    ciphertext = [ciphertext[i:i+ngram] for i in range(0, len(ciphertext), ngram)]
    for ngram in ciphertext:
        ngrams.add(ngram)

    # Sorts the list
    for ngram in ngrams:
        frequencies.append(100 * ciphertext.count(ngram) / len(ciphertext))
    sorting_key = lambda pair : pair[1] # ensures the list is sorted by the frequency
    pairs = sorted(zip(ngrams, frequencies), key=sorting_key, reverse=True)

    print("================================= Frequencies ================================\n")
    draw_graph(pairs, 20, 1, 1)
    
    print(f"\n Total number of characters = {len(pairs)}")

def word_frequency(ciphertext):
    words = []
    frequencies = []
    word_length = 3
    cipherwords = [ciphertext[i:i+word_length] for i in range(0, len(ciphertext), word_length)]
    for word in cipherwords:
        if not word in words:
            words.append(word)
    for word in words:
        frequencies.append(100 * cipherwords.count(word) / len(ciphertext))
    pairs = sorted(zip(words, frequencies), key=lambda pair : pair[1], reverse=True)
    print("============================== Word frequencies ==============================\n")
    draw_graph(pairs, 10, 1, 1)
    
    print(f"\n Total number of distinct words = {len(pairs)}")

def word_length(ciphertext):
    totals = []
    factors = []
    for num in range(1, 42):
        if len(ciphertext) % num == 0:
            factors.append(num)
    for factor in factors:
        words = set()
        for i in range(0, len(ciphertext), factor):
            words.add(ciphertext[i:i+factor])
        totals.append(len(words))
        print(words)

    pairs = sorted(zip(factors, totals), key=lambda pair : pair[0])
    print("=========================== Distinct words of length x ==========================\n")
    draw_graph(pairs, 50, 1, 1)

def index_of_coincedence(ngram):
    ngrams = [ciphertext[i:i+ngram] for i in range(0, len(ciphertext), ngram)]
    ciphertext_ioc = cc.index_of_coincedence(ngrams)
    expected_ioc = cc.EXPECTED_IOC

    print("\n============================= Index of coincedence ============================\n")
    
    print(f" Ciphertext =\t{ciphertext_ioc}")
    print(f" Expected   =\t{expected_ioc}")

def period(max, ngram):
    print("\n=================================== Period ====================================\n")

    letters = set()
    data = []
    ngrams = [ciphertext[i:i+ngram] for i in range(0, len(ciphertext), ngram)]
    for letter in ngrams:
        letters.add(letter)
    for period in range(1, max+1):
        total = 0
        for start in range(period):
            slice = ""
            for index in range(0, len(ngrams), period):
                slice += ngrams[index]
            total += cc.index_of_coincedence(slice)
        data.append(total / period * 100)

    labels = list(x for x in range(1, max+1))
    pairs = sorted(zip(labels, data), key=lambda pair : pair[0])
    draw_graph(pairs, 200, 10, 2)

def factors():
    print("\n=================================== Factors ===================================\n")
    length = len(ciphertext)
    factors_list = set()
    for i in range(2, int(math.sqrt(length))):
        factor = i
        while length % factor == 0:
            factors_list.add(factor)
            factors_list.add(length // factor)
            factor *= i

    factors_list = sorted(factors_list)

    print(f" Ciphertext length = {length}")
    print(f" Factors of {length} are {factors_list}")

withspaces = cc.get_ciphertext()

ciphertext = cc.remove_whitespace(withspaces)
print(len(ciphertext))

frequency(ciphertext, 1)
# word_length(ciphertext)
# index_of_coincedence(1)
period(16, 1)
# period(30, 2)
# period(30, 3)
# factors()

print()
