input = open(r'Cipher challenge\input.txt', 'r').read()

def substring(text, start, length, step=1):
    substr = str()
    if text != 1:
        for index in range(start, step * (start + length), step):
            substr += text[index]
    else:
        return text[start:start+length]
    return substr

def reverse(text):
    reversed = str()
    for index in range(len(text)-1, -1, -1):
        reversed += text[index]
    return reversed

output = substring(input, 0, 70)

open(r'Cipher challenge\output.txt', 'w').write(output)
