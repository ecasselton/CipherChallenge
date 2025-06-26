import cipherchallenge as cc

def decipher(ciphertext: str, key: list):
    inverse_key = []
    for num in key:
        inverse_key.append(-num)
    return encipher(ciphertext, inverse_key)


def encipher(plaintext: str, key: list):
    ciphertext = ""
    key_length = len(key)
    key_index = 0
    index = 0
    while index < len(plaintext):
        char = plaintext[index]
        value = ord(char.upper()) - 65
        if value >= 0 and value < 26:
            new_value = (value + key[key_index]) % 26
            ciphertext += chr(new_value+65)
            key_index = (key_index + 1) % key_length
        else:
            ciphertext += char
        index += 1
    return ciphertext

key = [(ord(x)-96) for x in "viginere"]
print(key)
print(encipher(cc.remove_punctuation(cc.get_ciphertext()), [5, 8, 12, 4, 7, 6, 10]))
