#Baconian Cipher

alphabet = input().split(' ')
print(alphabet)

text = open(r'Cipher challenge\input.txt', 'r').readline()

output = ''

for letter in text:
    if alphabet.index(letter) < 13:
        output += 'A'
    else:
        output += 'B'

open(r'Cipher challenge\output.txt', 'w').write(output)