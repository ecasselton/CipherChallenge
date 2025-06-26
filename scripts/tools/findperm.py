import cipherchallenge as cc
from itertools import permutations

ciphertext = cc.remove_whitespace(cc.get_ciphertext())

rows = [ciphertext[i:i+7] for i in range(0, len(ciphertext), 7)]

permutations = permutations(range(7), 7)

for perm in permutations:
    counts = {'|': 0, '\\': 0, '/': 0}
    j = 0
    row = 0
    done = False
    while row < len(rows) and not done:
        for i in perm:
            counts[rows[row][i]] += 1
            if counts[rows[row][i]] > 1:
                break
                done = True
            j+=1
            if j == 3:
                j = 0
                counts = {'|': 0, '\\': 0, '/': 0}
            row += 1
    if row == len(rows):
        print(perm)

