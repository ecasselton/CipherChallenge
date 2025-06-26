FILENAME = "/home/elliot/OneDrive/Programming/CipherChallenge/Data/dictionary.txt"

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dictionary = []
words = []
splits = []

longest = 0
length = 0
letter = 0
place = 0
input_mode = 0
lookback = 0
word =''
check = ''


def original_loop():
    global input_mode
    while input_mode != '1' and input_mode != '2':
        input_mode = input('INPUT MODE(1, 2): ')
    input_mode = int(input_mode)

def string(_list_, character):
    paragraph = ''
    for word in _list_:
        paragraph += word + character
    return paragraph

def array(chars):
    _list_ = []
    for char in chars:
        _list_.append(char)
    return _list_

def remove_punctuation():
    global text
    letters = array(text)
    for letter in letters:
        if letter.upper() not in alphabet:
            letters.remove(letter)
    text = string(letters, '')

def add_words():
    global dictionary, longest
    done = False
    word = ''
    filename = FILENAME
    with open(filename, 'r') as file:
        while not done:
            line = file.readline()
            if line == '':
                done = True
            if len(line) > longest:
                longest = len(line)
            dictionary.append(line[:len(line) - 1])

def add_word(word):
    filename = FILENAME
    with open(filename, 'a') as file:
        file.write(word.upper() + '\n')

original_loop()
add_words()

while True:
    if input_mode == 2:
        word = input('INPUT CHECK WORD: ')
        if word.upper() in dictionary:
            print(word + ' is in the dictionary')
        else:
            if input(word + ' isn\'t in the dictonary, would you like to add it? (Y/N) ').upper() == 'Y':
                add_word(word)
        original_loop()

    elif input_mode == 1:
        text = input('INPUT TEXT: ').upper()

        remove_punctuation()

        words = ['']

        length = 0
        letter = 0
        place = 0
        input_mode = 0
        word = ''
        done = False
        length = longest

        while letter < len(text):
            splits = []

            sum = 0
            check = ''
            word = text[letter:letter + length]
            lookback = len(words)-1
            
            while len(check) < longest and lookback > -1:
                check = words[lookback] + check
                splits.insert(0, len(words[lookback]))
                lookback -= 1

            place = len(check)

            while place > -1 and word not in dictionary:
                #constantly reduces the length of word once it gets to 1 long, it takes a letter from the previous word (check)

                if length == 1 and word not in dictionary:
                    length = longest
                    place -= 1
                    word = text[letter:letter + length]

                length -= 1
                word = check[place:len(check)] + text[letter:letter + length]

            if word in dictionary:
                check = check[:place]
                num = 0

                for pos in splits:
                    lookback += 1
                    words[lookback] = check[:pos]
                    check = check[pos:]
                
                words.append(word)
            
            else:
                words.append(text[letter])
                length = 1
                
            letter += length
            length = longest
            lookback = len(words)-1

        print(string(words, ' '))
        original_loop()
