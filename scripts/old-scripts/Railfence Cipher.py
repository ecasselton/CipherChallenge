# bigrams = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ES', 'ON', 'ST', 'NT', 'EN', 'AT', 'ED', 'ND', 'TO', 'OR', 'EA', 'TI', 'AR', 'TE', 'NG', 'AL', 'IT', 'AS', 'IS', 'HA', 'ET', 'SE', 'OU', 'OF']
# trigrams = ['THE', 'AND', 'ING', 'ENT', 'ION', 'HER', 'FOR', 'THA', 'NTH', 'INT', 'ERE', 'TIO', 'TER', 'EST', 'ERS', 'ATI', 'HAT', 'ATE', 'ALL', 'ETH', 'HES', 'VER', 'HIS', 'OFT', 'ITH', 'FTH', 'STH', 'OTH', 'RES', 'ONT']
# bifreq = [2.71, 2.33, 2.03, 1.78, 1.61, 1.41, 1.32, 1.32, 1.25, 1.17, 1.13, 1.12, 1.08, 1.07, 1.07, 1.06, 1.0, 0.99, 0.98, 0.98, 0.89, 0.88, 0.88, 0.87, 0.86, 0.83, 0.76, 0.73, 0.72, 0.71]
# trifreq = [1.8, 0.73, 0.72, 0.42, 0.42, 0.36, 0.34, 0.33, 0.33, 0.32, 0.31, 0.31, 0.3, 0.28, 0.28, 0.26, 0.26, 0.25, 0.25, 0.24, 0.24, 0.24, 0.24, 0.22, 0.21, 0.21, 0.21, 0.21, 0.21, 0.2]

possibilities = []
text = input('INPUT TEXT: ')
factor = 2
first = text[0]
text = text[1:]
text_copy = text
fence = []

def stringed(array):
    string = ''
    for each in array:
        string += each
    return string

def insert(string, pos, char):
    string = [str(x) for x in str(string)]
    string[pos] = char
    return stringed(string)

def check(possibilities, bifreq, trifreq):
    text_copy_bigrams = []
    text_copy_trigrams = []
    closest = 0
    largest = 0
    binum = 0
    trinum = 0
    num = 0
    for text_copy in possibilities:
        for bigram in bigrams:
            text_copy_bigrams.append(text_copy.count(bigram)/len(text_copy))
        for trigram in trigrams:
            text_copy_trigrams.append((text_copy.count(trigram)/len(text_copy)))
        for freq in bifreq:
            binum += freq * text_copy_bigrams[bifreq.index(freq)]
        for freq in trifreq:
            trinum += freq * text_copy_trigrams[trifreq.index(freq)]
        num = binum + trinum
        if num > largest:
            largest = num
            closest = possibilities.index(text_copy)
        num = 0
        binum = 0
        trinum = 0
        text_copy_bigrams = []
        text_copy_trigrams = []
    return possibilities[closest]

for each in range(8):
    text_copy = stringed(text.split(' '))
    width = int((len(text_copy))/(factor-1))

    for each in range(factor):
        fence.append('')

    column = 0
    row = 1
    index = 0
    num = 0
    directions = {0:1, 1:-1}

    while num < len(text_copy):
        if row == 0:
            index = 0
            fence[row] += ' '
        elif row == len(fence)-1:
            index = 1
            fence[row] += ' '
        fence[row] += 'x'
        row += directions[index]
        num += 1

    for each in range(len(fence)):
        for char in range(fence[each].count('x')):
            fence[each] = insert(fence[each], fence[each].index('x'), text_copy[0])
            text_copy=text_copy[1:]

    index = 0
    message = first
    end = False

    while index <= width:
        for each in range(len(fence)):
            if len(fence[each]) > index:
                message += fence[each][index]
        index += 1
        for each in range(len(fence)-1, -1, -1):
            if len(fence[each]) > index:
                message += fence[each][index]
        index += 1

    possibilities.append(stringed(message.split(' ')))

    for row in fence:
        print(row)
    
    fence = []

    factor += 1

print()
print(check(possibilities, bifreq, trifreq))
