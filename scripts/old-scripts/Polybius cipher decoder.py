coords = []
text = input('INPUT TEXT: ')
for pos in range(int(0), len(text)-1, 2):
    coords.append(text[pos:pos+2])

row = []

for y in range(5):
    for each in coords:
        if int(each[0]) == y + 1:
            row.append(each[1])
    print(row)
    input()