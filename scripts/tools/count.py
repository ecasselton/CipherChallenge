import cipherchallenge as cc

ciphertext = cc.remove_whitespace(cc.get_ciphertext())
x = 3

for i in range(0, len(ciphertext), x):
    threes = 0
    for char in ('/', '|', '\\'):
        count = 0
        for j in range(i, i+x):
            if ciphertext[j] == char:
                count += 1
        if count > 1:
            threes += 1
    if threes:
        print(i/x/3)
