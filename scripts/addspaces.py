import cipherchallenge as cc

text = []

with open("input.txt") as output:
    text = [" "]
    text += [char for char in cc.remove_punctuation(output.read())]

dictionary = []

with open("data/dictionary.txt", "rt") as words_file:
    dictionary = words_file.readlines()[:-1]

words = {}

for word in dictionary:
    a = 0
    b = 1
    word = word[:-1]
    while b < len(text):
        if text[b] != word[b-a-1]:
            a += 1
            b = a
        elif b-a == len(word):
            words[a+1] = word
            text[a+1:b+1] = [' '] * len(word)
            a = b
        b += 1

word = ""
for a in range(len(text)):
    if text[a] != ' ':
        word += text[a]
    elif word:
        words[a-len(word)] = word
        word = ""
if word:
    words[a] = word

spaced_message = ""
words = sorted(words.items())
for index, word in words:
    spaced_message += word
    spaced_message += " "
    print(word, end=" ")

print()

cc.write_plaintext(spaced_message)
