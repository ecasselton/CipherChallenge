import cipherchallenge as cc

def decipher(ciphertext: str, shift: int):
    plaintext = ""
    for char in ciphertext:
        ascii = ord(char.upper())
        if ascii > 64 and ascii <= 64 + 26:
            plaintext += chr((ascii - 65 + 26 - shift) % 26 + 65)
        else:
            plaintext += char
    return plaintext

def get_shift(ciphertext: str):
    # FREQS = cc.get_ngram_frequencies((1,))
    best_fitness = 0
    best_shift = 0
    for shift in range(26):
        deciphered_text = decipher(ciphertext, shift)
        fitness = cc.get_fitness(deciphered_text, (1,))
        if fitness > best_fitness:
            best_fitness = fitness
            best_shift = shift

    return best_shift

if __name__ == "__main__":
    ciphertext = cc.get_ciphertext()
    shift = get_shift(ciphertext)
    plaintext = decipher(ciphertext, shift)
    print(plaintext)
    print()
    print(shift)

    cc.write_plaintext(plaintext)
