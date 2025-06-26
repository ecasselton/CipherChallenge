import cipherchallenge as cc

def bigram_frequencies(ciphertext):
    ngrams = []
    frequencies = []
    for ngram in ciphertext:
        if not ngram in ngrams:
            ngrams.append(ngram)
    for ngram in ngrams:
        frequencies.append(100 * ciphertext.count(ngram) / len(ciphertext))
    pairs = sorted(zip(frequencies, ngrams), reverse=True)
    return pairs

ciphertext = cc.remove_whitespace(cc.get_ciphertext())
ciphertext = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
ciphertext_frequencies = bigram_frequencies(ciphertext)
freqs = cc.get_ngram_frequencies((2,))
global_freqs = sorted(zip(freqs.values(), freqs.keys()), reverse=True)

plaintext = [""] * len(ciphertext)
print(ciphertext_frequencies)
print(freqs)
print(ciphertext)

for pair in range(len(ciphertext_frequencies)):
    frequency, bigram = ciphertext_frequencies[pair]
    for index in range(len(ciphertext)):
        if ciphertext[index] == bigram:
            try:
                plaintext[index] = global_freqs[pair][1]
            except:
                plaintext[index] = "  "
    print(f"{pair}/{len(ciphertext_frequencies)}")

for bigram in plaintext:
    print(bigram, end="")
