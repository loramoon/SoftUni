rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

command = input().split()

while command[0] != 'END':
    row, col, value = [int(el) for el in command[1:]]
    if col < 0 or row < 0 or col >= rows or row >= rows:
        print('Invalid coordinates')
    else:
        if command[0] == 'Add':
            matrix[row][col] += value
        elif command[0] == 'Subtract':
            matrix[row][col] -= value
    command = input().split()

for row in matrix:
    print(*row, sep=' ')