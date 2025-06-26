import cipherchallenge as cc
ciphertext = cc.remove_whitespace(cc.get_ciphertext())

transliterated = ""
x = 2
cipherwords = [ciphertext[i:i+x] for i in range(0, len(ciphertext), x)]
# print(cipherwords)
alphabet = [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
# words = ['|\\/', '|/\\', '\\/|', '/|\\', '/\\|', '\\|/']
# words = ['/|\\', '/\\|', '|/\\', '\\/|', '|\\/', '\\|/']
words = []
# print(alphabet)

for word in cipherwords:
    if word not in words:
        words.append(word)
    print(words.index(word))
    transliterated += alphabet[words.index(word)]

cc.write_plaintext(transliterated)
