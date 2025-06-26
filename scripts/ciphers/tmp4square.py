import cipherchallenge as cc

square = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'K',
    'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]

template = [square.copy(), [], [], square.copy()]

with open("Data/dictionary.txt") as dictionary:
    words = dictionary.readlines()

ciphertext = cc.remove_punctuation(cc.get_ciphertext())

def generate_key(keywords):
    key = template
    for i in range(2):
        square = []
        for letter in keywords[i]:
            if letter not in square:
                square.append(letter)
        for char in range(ord(letter), ord(letter)+26):
            ascii = chr((char-65)%26+65)
            if ascii != 'J' and ascii not in square:
                square.append(ascii)
        key[i+1] = square
    return key

def decipher(ciphertext, squares):
    plaintext = ""
    # bigrams = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    
    for index in range(0, len(ciphertext), 2):
        bigram = ciphertext[index:index+2]
        poses = [squares[1].index(bigram[0]), squares[2].index(bigram[1])]
        rows = [poses[0] //5, poses[1] //5]
        cols = [poses[0] % 5, poses[1] % 5]
        plaintext += squares[0][rows[0] * 5 + cols[1]]
        plaintext += squares[3][rows[1] * 5 + cols[0]]
    
    return plaintext

FREQS = cc.get_ngram_frequencies((1,2,3))
best_fitness = 0
best = ""
i = 0
while i < len(words):
    if 'J' in words[i]:
        del words[i]
    else:
        i += 1

for word1 in words:
    for word2 in words:
        key = generate_key([word1[:-1], word2[:-1]])
        plaintext = decipher(ciphertext, key)
        fitness = cc.get_fitness(plaintext, FREQS)
        if fitness > best_fitness:
            best_fitness = fitness
            best = plaintext

print(best)
#print(generate_key(["PLAYFAIR", "EXAMPLE"]))
