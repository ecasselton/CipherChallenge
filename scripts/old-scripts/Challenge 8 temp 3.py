dictionary = open(r'Cipher challenge\dictionary.txt', 'r').readlines()

for word in dictionary:
    if len(word) <= 11 and len(word) > 2:
        open(r'Cipher challenge\words.txt', 'a').write(word)