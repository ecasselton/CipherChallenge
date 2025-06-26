#Anti-anagrammer

input = open(r'Cipher challenge\input.txt', 'r').read()
dictionary = open(r'Cipher challenge\dictionary.txt', 'r').readlines()

letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

words = list()

for each in dictionary:
    index = 0
    word = each[:-1]
    while index < len(word) and input.count(word[index]) >= word.count(word[index]):
        index += 1
    if not (index < len(word)):
        words.append(word)

with open(r'Cipher challenge\output.txt', 'w') as filename:
    for word in words:
        filename.write(word)
        filename.write('\n')