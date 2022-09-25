rows, cols = [int(el) for el in input().split()]
matrix = []
temp = []
for row in range(rows):
    matrix.append([el for el in input().split()])

command = input().split()
while command[0] != "END":
    swap = command[0]
    if len(command) != 5 or swap != 'swap':
        print("Invalid input!")
        command = input().split()
        continue
    else:
        row1, col1, row2, col2 = [int(el) for el in command[1:5]]
        if row1>rows or col1>cols or row2>rows or col2>cols:
            print("Invalid input!")
            command = input().split()
            continue
        temp.append(matrix[row1][col1])
        temp.append(matrix[row2][col2])
        matrix[row1][col1] = temp.pop()
        matrix[row2][col2] = temp.pop()
        for row in matrix:
            print(*row, sep=' ')
    command = input().split()
