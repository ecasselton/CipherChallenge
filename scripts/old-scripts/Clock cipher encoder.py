alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = ['O', 'A', 'H', 'K', 'P', 'E', 'V', 'Z', 'Q', 'B', 'I', 'L', 'R', 'F', 'W', '#', 'S', 'C', 'J', 'M', 'T', 'G', 'X', '+', 'N', 'D', 'U', 'Y']

#print(key)
num = 0
letter = 0

def go(_list_, index, aim):
    num = 0
    while index % len(_list_) != aim:
        index += 1
        num += 1
    return num

def string(_list_):
    string = ''
    for each in _list_:
        string += str(each)
    return string

def encode(text):
    global num
    text = [str(x) for x in str(text)]
    letters = []
    for each in text:
        if each.upper() in key:
            thing = go(alphabet, num, alphabet.index(each.lower()))
            num += thing
            letters.append(key[num % 28].upper())
        else:
            letters.append(each)
    print(string(letters))

encode('thequickbrownfoxjumpsoverthelazydogsback')

#SC+ULO#Q+LWOXAY+XKUOQNDWBFTKUCXHTS
