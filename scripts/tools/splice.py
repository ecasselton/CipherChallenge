import cipherchallenge as cc

period = 7
ciphertext = cc.remove_whitespace(cc.get_ciphertext())
half = int(len(ciphertext)/2)
new_text = ""
for i in range(half):
    new_text += ciphertext[i] + ciphertext[i+half]

print(new_text)
