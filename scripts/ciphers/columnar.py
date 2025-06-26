import cipherchallenge as cc

def decipher(ciphertext, permutation, write=0, read=1):
    # Modes (described as the process of encryption):
    # 0 - Across
    # 1 - Down

    width = len(permutation)
    height = len(ciphertext) // width
    cells = [[""] * width for col in range(height)]
    plaintext = ""
    if read == 0:
        for row in range(height):
            for col in range(width):
                cells[row][col] = ciphertext[row * width + permutation.index(col)]
    elif read == 1:
        for col in range(width):
            for row in range(height):
                cells[row][col] = ciphertext[row + height * permutation.index(col)]
    if write == 0:
        for row in range(height):
            for col in range(width):
                plaintext += cells[row][col]
    elif write == 1:
        for col in range(width):
            for row in range(height):
                plaintext += cells[row][col]

    return plaintext

if __name__ == "__main__":
    ciphertext = cc.remove_whitespace(cc.get_plaintext())
    plaintext = decipher(ciphertext, [0, 1])
    print(plaintext)
    cc.write_plaintext(plaintext)
