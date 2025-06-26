alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text = input('INPUT TEXT: ').upper()
key = text
msg = ''

for each in range(10):
    text = text[1:]
    for letter in range(len(text)):
        msg += alphabet[(alphabet.index(text[letter])+alphabet.index(key[letter])) % 26]
    print(msg)
    msg = ''