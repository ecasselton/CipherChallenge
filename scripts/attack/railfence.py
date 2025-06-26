import cipherchallenge as cc

def stringed(array):
    string = ''
    for each in array:
        string += each
    return string

def insert(string, pos, char):
    string = [str(x) for x in str(string)]
    string[pos] = char
    return stringed(string)

def decipher(ciphertext, num_rows):
    copy = ciphertext
    width = len(ciphertext) // (num_rows * 2 - 2)

    fence = []

    modulus = num_rows * 2 - 2
    for row in range(num_rows):
        fence.append(ciphertext[row*width : (row+1) * width])

    print(fence)
    i = 0
    message = ""
    while i < width:
        row = i % modulus
        if row < num_rows:
            message += fence[row]
        else:
            message += fence[2 * num_rows - row - 1]
        i += 1

    print(message)

    # return cc.remove_punctuation(message)


ciphertext = cc.get_ciphertext()
possibilities = []
for i in range(4, 5):
    possibilities.append(decipher(cc.remove_punctuation(ciphertext), i))

print(possibilities)

