def get_ciphertext():
    with open("/home/mrchess/OneDrive/Programming/CipherChallenge/input.txt", "rt") as input_file:
        input_text = input_file.read().upper()
    return input_text

def write_plaintext(plaintext: str):
    with open("/home/mrchess/OneDrive/Programming/CipherChallenge/output.txt", "wt") as output_file:
        output_file.write(plaintext)

def remove_punctuation(text: str):
    filtered_text = ""
    for char in text:
        ascii_code = ord(char.upper())
        if ascii_code > 64 and ascii_code <= 64 + 26:
            filtered_text += char.upper()
    return filtered_text

def calculate_ngram_frequencies(ns: int):
    with open("/home/mrchess/OneDrive/Programming/CipherChallenge/Data/Sample.txt", "rt") as sample:
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
    with open("/home/mrchess/OneDrive/Programming/CipherChallenge/Data/NgramFrequencies.txt", "wt") as ngram_frequencies:
        for n in range(1, ns+1):
            for ngram, count in ngram_count[n].items():
                frequency = round(count / sample_length, 4)
                if frequency > 0.001:
                    ngram_frequencies.write(f"{ngram}:{count/len(sample_text)}\n")

def get_ngram_frequencies(ns):
    frequencies = {}
    with open("/home/mrchess/OneDrive/Programming/CipherChallenge/Data/NgramFrequencies.txt") as ngram_frequencies:
        lines = ngram_frequencies.readlines()
    for line in lines:
        ngram, frequency = line.split(":")
        if len(ngram) in ns:
            frequencies[ngram] = float(frequency)
    return frequencies

def chi_squared(text: str, string: str):
    # Format for weights = [mono, di, tri] -grams
    weights = [5, 4, 4]
    observed_frequency = text.count(string) / len(text)
    expected_frequency = FREQS[string]
    return ((observed_frequency - expected_frequency) ** 2) / weights[len(string) - 1]

def get_fitness(text: str):
    fitness = 0
    for string in FREQS.keys():
        fitness += chi_squared(text, string)
    return 1 / fitness

calculate_ngram_frequencies(3)
FREQS = get_ngram_frequencies(3)
