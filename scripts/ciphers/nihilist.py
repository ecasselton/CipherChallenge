import cipherchallenge as cc

ciphertext = cc.get_ciphertext()
words = ciphertext.split(' ')
for i in range(len(words)):
    words[i] = int(words[i])

# Prints out the index of coincedence for possible periods
for period in range(2, 10):
    slice = []
    for word in range(0, len(words), period):
        slice.append(words[word])
    print(f"{period}:{cc.index_of_coincedence(slice)}")

# I figured this key length out from the above chunk of code
key_length = 7

# This prints out the maximum and minimum of each slice,
# Hinting at what value has been added
for offset in range(key_length):
    slice = []
    for word in range(offset, len(words), key_length):
        slice.append(words[word])

    print(min(slice), max(slice))

# I figured this key out with a pen and paper, using the
# above code (remember that no digits can be 6 or more!!!)
key = [55, 14, 23, 45, 51, 55, 44]

plaintext = []
for i in range(len(words)):
    plaintext.append(words[i]-key[i % key_length])

output = ""
for word in plaintext:
    output += str(word) + ' '

print(output)
