import cipherchallenge as cc

ciphertext = cc.remove_whitespace(cc.get_ciphertext())

index = 0
shift = 0
period = 5
plaintext = ""
while index < len(ciphertext):
    plaintext += chr((ord(ciphertext[index])-65 - shift) % 26 + 65)
    if index % period == 3:
        shift += 1
    index += 1

print(plaintext)
cc.write_plaintext(plaintext)
