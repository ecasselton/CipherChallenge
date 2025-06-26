import cipherchallenge as cc

square = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

def decipher(ciphertext):
    plaintext = ""
    for index in range(0, len(ciphertext), 2):
        plaintext += square[int(ciphertext[index])-1][int(ciphertext[index+1])-1]
    return plaintext


ciphertext = cc.get_ciphertext()
plaintext = decipher(cc.remove_whitespace(ciphertext))
print(plaintext)
cc.write_plaintext(plaintext)
