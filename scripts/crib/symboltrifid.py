import cipherchallenge as cc
from random import randint, random

def decipher(ciphertext, period, key):
    blocks = [ciphertext[i:i+period] for i in range(0, len(ciphertext), period)]
    plaintext = ""
    for block in blocks:
        rect = [[]]
        j = 0
        for char in block:
            value = key.index(char)
            for i in (9, 3, 1):
                rect[j//len(block)].append(value // i)
                value %= i
                j += 1
                if (j % len(block) == 0):
                    rect.append([])

        for i in range(len(block)):
            plaintext += key[rect[0][i] * 9 + rect[1][i] * 3 + rect[2][i]]

    return plaintext

ciphertext = cc.remove_whitespace(cc.get_ciphertext())
crib = "LORDPALMERSTON" # Must be 2 * period - 1 or longer

cube = [
    [char for char in 'ABCDEFGHI'],
    [char for char in 'JKLMNOPQR'],
    [char for char in 'STUVWXYZ+'],
]

# \\/ \/| |\| |\| //| |/\ \//

for period in range(1, 100):
    if len(ciphertext) % (3 * period) == 0:
        blocks = [ciphertext[i:i+3*period] for i in range(0, len(ciphertext), 3 * period)]
        ordered = []
        for block in blocks:
            shuffled = [""] * period
            j = 0
            for char in block:
                shuffled[j] += char
                if len(shuffled[j]) == 3:
                    j += 1

            for row in range(3):
                for col in range(period):
                    if (row * period + col) % 3 == 0:
                        ordered.append("")
                    ordered[-1] += shuffled[col][row]

        words = set()
        for word in ordered:
            words.add(word)

        print(len(words))

# for i in range(2 * period - 1):
#     rect = [[]]
#     j = 0
#     for char in block:
#         value = cube.index(char)
#         for i in (9, 3, 1):
#             rect[j//len(block)].append(value // i)
#             value %= i
#             j += 1
#             if (j % len(block) == 0):
#                 rect.append([])

# for i in range(0, len(ciphertext), len(crib)):
#     print(key)
#     print(decipher(ciphertext, PERIOD, key))

# period = 7
# plaintext = decipher(ciphertext, period, key)
# print(plaintext)
