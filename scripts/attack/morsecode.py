import cipherchallenge as cc

letters = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
numbers = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

morse_code = cc.get_ciphertext()

plaintext = ""
words = morse_code.split('/')
print(words)
for word in words:
    chars = word.split(" ")
    for char in chars:
        if char in letters:
            plaintext += chr(65 + letters.index(char))
        elif char in numbers:
            plaintext += str(numbers.index(char))
        else:
            print(f"Unrecognised morse code sequence [{char}] found!! (continuing with the rest of the input text)")
    plaintext += " "

cc.write_plaintext(plaintext)
