def get_next_position(direction, row, col):
    if direction == 'up':
        return row-1, col
    if direction == 'down':
        return row+1, col
    if direction == 'left':
        return row, col-1
    if direction == 'right':
        return row, col+1


presents = int(input())
n = int(input())
matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0
good_presents = 0
for i in range(n):
    matrix.append([el for el in input().split()])
    for j in range(n):
        if matrix[i][j] == 'S':
            santa_row = i
            santa_col = j
        elif matrix[i][j] == 'V':
            nice_kids += 1

while True:
    command = input()
    if command == 'Christmas morning':
        break
    matrix[santa_row][santa_col] = '-'

    santa_row, santa_col = get_next_position(command, santa_row, santa_col)
    if matrix[santa_row][santa_col] == 'V':
        presents -= 1
        good_presents += 1
    elif matrix[santa_row][santa_col] == 'C':
        if matrix[santa_row][santa_col-1] == 'V' and presents:
            good_presents += 1
            presents -= 1
            matrix[santa_row][santa_col - 1] = '-'
        elif matrix[santa_row][santa_col-1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_col - 1] = '-'
        if matrix[santa_row][santa_col+1] == 'V' and presents:
            good_presents += 1
            presents -= 1
            matrix[santa_row][santa_col + 1] = '-'
        elif matrix[santa_row][santa_col+1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_col + 1] = '-'
        if matrix[santa_row-1][santa_col] == 'V' and presents:
            good_presents += 1
            presents -= 1
            matrix[santa_row - 1][santa_col] = '-'
        elif matrix[santa_row-1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row - 1][santa_col] = '-'
        if matrix[santa_row+1][santa_col] == 'V' and presents:
            good_presents += 1
            presents -= 1
            matrix[santa_row + 1][santa_col] = '-'
        elif matrix[santa_row+1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row + 1][santa_col] = '-'

    matrix[santa_row][santa_col] = 'S'

    if presents == 0 or good_presents == nice_kids:
        break



if presents == 0 and good_presents<nice_kids:
    print("Santa ran out of presents!")
for ma in matrix:
    print(*ma)
if nice_kids == good_presents:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids-good_presents} nice kid/s.")