import cipherchallenge as cc

string = cc.get_ciphertext()
reversed = string[::-1]
cc.write_plaintext(reversed)
print(reversed)
