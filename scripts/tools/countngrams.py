import cipherchallenge as cc
ngram = 3
cipherwords = cc.remove_whitespace(cc.get_ciphertext())
ngrams = set()
frequencies = []

# Creates a list of the ngrams in the ciphertext
indices = []
cipherwords = [cipherwords[i:i+ngram] for i in range(0, len(cipherwords), ngram)]
for i in range(len(cipherwords)):
    ngrams.add(cipherwords[i])
    if cipherwords[i] == "|//":
        indices.append(i)

for ngram in ngrams:
    frequencies.append(cipherwords.count(ngram))

print(sorted(zip(ngrams, frequencies), key=lambda pair : pair[1]))
print(len(ngrams))
# print(indices)
