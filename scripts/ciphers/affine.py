import cipherchallenge as cc

def mod_inverse(num):
    inverse = 0
    while inverse % 26 != 1:
        inverse = (inverse + num)
    return inverse/num

def decipher(ciphertext: str, a: int, b: int):
    plaintext = ""
    for char in ciphertext:
        ascii = ord(char.upper())
        if ascii >= 65 and ascii < (65+26):
            plaintext += chr(int(65 + (mod_inverse(a) * (ascii - 65 - b)) % 26))
        else:
            plaintext += char
    return plaintext

def encipher(plaintext: str, a: int, b: int):
    ciphertext = ""
    for char in plaintext:
        ascii = ord(char.upper())
        if ascii >= 65 and ascii < (65+26):
            ciphertext += chr(65 + (a * (ascii-65)+b) % 26)
        else:
            ciphertext += char
    return ciphertext
