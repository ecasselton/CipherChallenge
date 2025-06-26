import cipherchallenge as cc

text = []

with open("output.txt") as output:
    text = [char for char in cc.remove_punctuation(output.read())]

dictionary = []

with open("data/dictionary.txt", "rt") as words_file:
    dictionary = words_file.readlines()[:-1]

words = {}

for word in dictionary:
    a = 0
    word = word[:-1]
    for b in range(len(text)):
        if text[b] != word[b-a-1]:
            a = b
        elif b-a == len(word):
            words[a+1] = word
            text[a+1:b+1] = [' '] * len(word)
            a = b

word = ""
for a in range(len(text)):
    if text[a] != ' ':
        word += text[a]
    elif word:
        words[a-len(word)] = word
        word = ""
if word:
    words[a] = word

words = sorted(words.items())
for index, word in words:
    print(word, end=" ")
