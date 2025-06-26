BIGRAMS = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ES', 'ON', 'ST', 'NT', 'EN', 'AT', 'ED', 'ND', 'TO', 'OR', 'EA', 'TI', 'AR', 'TE', 'NG', 'AL', 'IT', 'AS', 'IS', 'HA', 'ET', 'SE', 'OU', 'OF']
TRIGRAMS = ['THE', 'AND', 'ING', 'ENT', 'ION', 'HER', 'FOR', 'THA', 'NTH', 'INT', 'ERE', 'TIO', 'TER', 'EST', 'ERS', 'ATI', 'HAT', 'ATE', 'ALL', 'ETH', 'HES', 'VER', 'HIS', 'OFT', 'ITH', 'FTH', 'STH', 'OTH', 'RES', 'ONT']
BIFREQ = [2.71, 2.33, 2.03, 1.78, 1.61, 1.41, 1.32, 1.32, 1.25, 1.17, 1.13, 1.12, 1.08, 1.07, 1.07, 1.06, 1.0, 0.99, 0.98, 0.98, 0.89, 0.88, 0.88, 0.87, 0.86, 0.83, 0.76, 0.73, 0.72, 0.71]
TRIFREQ = [1.8, 0.73, 0.72, 0.42, 0.42, 0.36, 0.34, 0.33, 0.33, 0.32, 0.31, 0.31, 0.3, 0.28, 0.28, 0.26, 0.26, 0.25, 0.25, 0.24, 0.24, 0.24, 0.24, 0.22, 0.21, 0.21, 0.21, 0.21, 0.21, 0.2]

lines = open(r'Cipher challenge\output-DESKTOP-8SMNEIF.txt').readlines()
dictionary = open(r'Cipher challenge\words.txt').readlines()

highest = 0
best = ''
for index, line in enumerate(lines):
    score = 0
    for bigram in BIGRAMS:
        if bigram in line:
            score += BIFREQ[BIGRAMS.index(bigram)]
    for bigram in TRIGRAMS:
        if bigram in line:
            score += TRIFREQ[TRIGRAMS.index(bigram)]
    if score > highest:
        highest = score
        best = line
    if index % int(len(lines)/100) == 0:
        print(index // int(len(lines)/100))

print(best, score)

