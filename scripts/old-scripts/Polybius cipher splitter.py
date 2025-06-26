grid = [
    ['A', 'B', 'C', 'D', 'E'], 
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'], 
    ['P', 'Q', 'R', 'S', 'T'], 
    ['U', 'V', 'W', 'X', 'Y']]

bigraphs = []
msg = ''
text = input('INPUT TEXT: ')

for each in range(0, len(text)-1, 2):
    bigraphs.append(text[each:each+2])

print(bigraphs)

for each in range(len(bigraphs)-1):
    bigraphs[each] = grid[int(bigraphs[each][0])-1][int(bigraphs[each][1])-1]

for each in bigraphs:
    msg += each

print(msg)
