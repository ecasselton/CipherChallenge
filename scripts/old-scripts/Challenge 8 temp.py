ciphertext = open(r'Cipher challenge\input.txt', 'r').read()

final_line = ciphertext[-36:-1]

plain_word = 'INFORMATION'

columns = []

for letter in plain_word:
    columns.append([])
    for index, char in enumerate(final_line):
        if char == letter:
            columns[-1].append(index)

def combinate(columns, combinations=[], combination=[], index=0):
    if index == len(columns):
        combinations.append(combination)
        return combinations
    else:
        for i in range(len(columns[index])):
            combinations = combinate(columns, combinations, combination + [columns[index][i]], index + 1)
    return combinations

combinations = combinate(columns)
# file = open(r'Cipher challenge\output.txt', 'a')

# for combination in combinations:
#     grid = ['' for row in range(41)]
#     for col in combination:
#         for row in range(len(grid)):
#             grid[row] += ciphertext[row*35+col-1]
#     for row in grid:
#         if row != plain_word:
#             file.write(row + '\n')

# file.close()
combination = [1, 10, 11, 26, 34, 12, 5, 27, 32, 28, 15]
grid = ['' for row in range(41)]
for col in combination:
    for row in range(len(grid)):
        grid[row] += ciphertext[row*35+col]
for row in grid:
    print(row)

print('done')