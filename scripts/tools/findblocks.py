import cipherchallenge as cc

ciphertext = cc.remove_whitespace(cc.get_ciphertext())

def is_balanced(string):
    pipes = string.count('|')
    forewards = string.count('/')
    backwards = string.count('\\')
    if pipes == forewards and forewards == backwards:
        return True
    return False

for length in range(3, 43, 1):
    balanced = True
    for i in range(0, len(ciphertext), length):
        if not is_balanced(ciphertext[i:i+length]):
            balanced = False
    if balanced:
        print(length)
