import cipherchallenge as cc

def decipher(ciphertext, key):
    print(key)
    inverted_key = [0] * 26
    for value in key:
        inverted_key[key[value]] = value
    print(inverted_key)
    plaintext = encipher(ciphertext, inverted_key)
    return plaintext

# def decipher(ciphertext, key):
#     deciphered_text = str()
#     for letter in ciphertext:
#         if letter in key:
#             deciphered_text += chr(key.index(letter) + 65)
#         else:
#             deciphered_text += letter
#     return deciphered_text

def encipher(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        code = ord(letter)-65
        if code >= 0 and code < 26:
            new_letter = chr((key[code]) % 26 + 65)
        else:
            new_letter = letter
        ciphertext += new_letter

    return ciphertext.upper()

print(decipher(cc.get_ciphertext(), [ord(char)-65 for char in "DSKJAPTGHZVMNECQWIFBLUOXRY"]))


