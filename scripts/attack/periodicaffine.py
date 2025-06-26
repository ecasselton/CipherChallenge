import cipherchallenge as cc
import viginere
import affine
import math

def get_key(ciphertext: str, period: int):
    key = []
    slices = viginere.slice_text(ciphertext, period)
    for slice in slices:
        key.append(affine.get_ab(slice))
    return key

def decipher(ciphertext, key):



if __name__ == "__main__":
    ciphertext = cc.get_ciphertext()

    # period = get_period(cc.remove_punctuation(ciphertext))
    period = 17
    key = get_key(cc.remove_punctuation(ciphertext), period)
    plaintext = viginere.decipher(ciphertext, key)

    print(plaintext)
    for shift in key:
        print(chr(shift + 65), end="")
    print()

    # cc.write_plaintext(plaintext)
