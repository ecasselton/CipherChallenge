def decipher(ciphertext: str, shift: int):
    plaintext = ""
    for char in ciphertext:
        ascii = ord(char.upper())
        if ascii > 64 and ascii <= 64 + 26:
            plaintext += chr((ascii - 65 + 26 - shift) % 26 + 65)
        else:
            plaintext += char
    return plaintext

def encipher(plaintext: str, shift: int):
    ciphertext = ""
    for char in plaintext:
        i = ord(char.upper()) - 65
        if i >= 0 and i < 26:
            ciphertext += chr((i + shift) % 26 + 65)
        else:
            ciphertext += char
    return ciphertext
