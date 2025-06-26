import cipherchallenge as cc
import ciphers.columnar as columnar

ciphertext = cc.remove_whitespace(cc.get_ciphertext())
x = 6

for i in range(1, 200):
    if len(ciphertext) % i == 0:
        key = [j for j in range(i)]
        shuffled = columnar.decipher(ciphertext, key, 0, 1)
        # print(shuffled)
        words = set()
        cipherwords = [shuffled[k:k+x] for k in range(0, x * len(ciphertext)//x, x)]
        for word in cipherwords:
            words.add(word)
        # if len(words) != 3**x:
        print(len(words))
