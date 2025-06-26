from statistics import mean


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = {}
text = ''

for each in alphabet:
    letters[each] = []

print(letters)

with open(r'C:\Users\Elliot Casselton\OneDrive - Yateley School\Documents\Python\Cipher challenge coding\text.txt') as paragraph:
    for line in paragraph:
        text += line.upper()

for letter in alphabet:
    last = 0
    for pos, each in enumerate(text):
        if letter == each:
            letters[letter].append(pos-last)
            last = pos
    letters[letter] = mean(letters[letter])

print(letters)

for key, value in letters.items():
    pass

print(letters)