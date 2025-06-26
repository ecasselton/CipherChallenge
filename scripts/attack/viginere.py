import cipherchallenge as cc
import ciphers.viginere as viginere
import caesar
import math

def slice_text(text, period):
    slices = []
    for start in range(period):
        slice = ""
        index = start
        while index < len(text):
            slice += text[index]
            index += period
        slices.append(slice)
    return slices

def get_period(ciphertext):
    iocs = []
    for period in range(2, 27):
        slices = slice_text(ciphertext, period)
        ioc_total = 0
        for slice in slices:
            ioc_total += cc.index_of_coincedence(slice)
        ioc = ioc_total / period
        iocs.append(ioc)

    mean = sum(iocs) / len(iocs)

    variance = 0
    for ioc in iocs:
        variance += (ioc - mean) ** 2 / len(iocs)

    standard_deviation = math.sqrt(variance)

    Zscores = []
    ZTHRESHOLD = 1.0

    for ioc in iocs:
        Zscores.append((ioc - mean) / standard_deviation)

    anomalies = [index + 2 for index in range(len(iocs)) if Zscores[index] > ZTHRESHOLD]

    # If it gives you a 'list index out of range' error, the ZTHRESHOLD is probably too high to detect the anomalous periods
    # TL;DR decrease ZTHRESHOLD
    return anomalies[0]


def get_key(ciphertext: str, period: int):
    key = []
    slices = slice_text(ciphertext, period)
    for slice in slices:
        key.append(caesar.get_shift(slice))
    return key


if __name__ == "__main__":
    ciphertext = cc.get_ciphertext()

    period = get_period(cc.remove_punctuation(ciphertext))
    key = get_key(cc.remove_punctuation(ciphertext), period)
    plaintext = viginere.decipher(ciphertext, key)

    print(plaintext)
    for shift in key:
        print(chr(shift + 65), end="")
    print()

    # cc.write_plaintext(plaintext)
