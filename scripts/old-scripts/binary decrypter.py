text = input('INPUT TEXT: ')
msg = ''
blocks = 5

for each in range(0, len(text)-1, blocks):
    msg += text[each:each+blocks]
    msg += ' '

print(msg)
