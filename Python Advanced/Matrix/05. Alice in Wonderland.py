def get_next_pos(row, col, direction):
    if direction == 'up':
        return row-1, col
    if direction == 'down':
        return row+1, col
    if direction == 'left':
        return row, col-1
    if direction == 'right':
        return row, col+1


size = int(input())
matrix = []
alice_row = 0
alise_col = 0
tea_bags = 0

for i in range(size):
    matrix.append([el for el in input().split()])
    for j in range(size):
        if matrix[i][j] == "A":
            alice_row = i
            alise_col = j

while tea_bags < 10:
    matrix[alice_row][alise_col] = '*'
    direction = input()
    next_row, next_col = get_next_pos(alice_row, alise_col, direction)

    if next_row <0 or next_col <0 or next_row >= size or next_col >= size:
        break

    alice_row, alise_col = next_row, next_col

    if matrix[alice_row][alise_col] in ('.', '*'):
        continue
    if matrix[alice_row][alise_col] == 'R':
        break
    tea_bags += int(matrix[alice_row][alise_col])

matrix[alice_row][alise_col] = '*'

if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(*row, sep=' ')
