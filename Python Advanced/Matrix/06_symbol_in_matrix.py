rows = int(input())
matrix = []

for row in range(rows):
    matrix.append(list(input()))

position = None
symbol = input()

for row in range(rows):
    for col in range(rows):
        if symbol == matrix[row][col]:
            position = (row, col)
            print(position)
            break
    if position:
        break
if not position:
    print(f"{symbol} does not occur in the matrix")
