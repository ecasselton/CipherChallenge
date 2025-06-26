import cipherchallenge as cc

def decipher(ascii_values: list):
    plaintext = ""
    for number in ascii_values:
        plaintext += chr(int(number))
    return plaintext


ascii_values = cc.get_ciphertext().split(' ')
plaintext = decipher(ascii_values)
cc.write_plaintext(plaintext)
print(plaintext)
