def decipher(ciphertext, key):
    inverted_key = []
    for value in key:
        inverted_key.append(-value)
    plaintext = encipher(ciphertext, inverted_key)
    return plaintext

def encipher(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        code = ord(letter)-65
        if code >= 0 and code < 26:
            new_letter = chr((key[code]) % 26 +65)
        else:
            new_letter = letter
        ciphertext += new_letter

    return ciphertext.upper()
