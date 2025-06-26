import cipherchallenge as cc

ciphertext = cc.get_ciphertext()
key = [char for char in input("INPUT KEY: ")]

def decipher(ciphertext, key):
    deciphered_text = str()
    for letter in ciphertext:
        if letter in key:
            deciphered_text += chr(key.index(letter) + 65)
        else:
            deciphered_text += letter
    return deciphered_text

while True:
    print(decipher(ciphertext, key))
    for letter in key:
        print(letter, end="")
    print()
    letter1, letter2 = [char.upper() for char in input()]
    index1, index2 = ord(letter1) - 65, ord(letter2) - 65
    key[index1], key[index2] = key[index2], key[index1]