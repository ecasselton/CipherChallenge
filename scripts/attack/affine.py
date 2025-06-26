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

def get_ab(ciphertext: str):
    best_ab = (1, 0)
    best_fitness = 0
    achoice = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for a in achoice:
        for b in range(26):
            deciphered_text = decipher(ciphertext, a, b)
            fitness = cc.get_fitness(deciphered_text, [1])
            if fitness > best_fitness:
                best_fitness = fitness
                best_ab = (a, b)
    return best_ab

ciphertext = cc.get_ciphertext()
a, b = get_ab(ciphertext)
plaintext = decipher(ciphertext, a, b)
print(plaintext)
print()
print(f"a={a}, b={b}")
print()

cc.write_plaintext(plaintext)
