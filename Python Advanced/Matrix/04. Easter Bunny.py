rows = int(input())
matrix = []
b_row = 0
b_col = 0
max_sum = -999999999
max_direction = ''
best_path = []
for row in range(rows):
    matrix.append(list(input().split()))
    for col in range(rows):
        if matrix[row][col] == "B":
            b_row = row
            b_col = col
            break

directions ={
    'right': lambda r, c: (r, c+1),
    'left': lambda r, c: (r, c-1),
    'down': lambda r, c: (r+1, c),
    'up': lambda r, c: (r-1, c)
}

for direction in directions:
    cur_sum = 0
    row, col = directions[direction](b_row, b_col)
    current_path = []

    while 0<=row<rows and 0<=col<rows and matrix[row][col]!='X':
        cur_sum += int(matrix[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)

    if cur_sum > max_sum:
        max_sum = cur_sum
        max_direction = direction
        best_path = current_path

print(max_direction)
print(*best_path, sep='\n')
print(max_sum)