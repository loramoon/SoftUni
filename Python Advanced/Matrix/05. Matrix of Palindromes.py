rows, cols = [int(el) for el in input().split()]
matrix = []

for row in range(rows):
    for col in range(cols):
        print(f'{chr(97+row)}{chr(97+row+col)}{chr(97+row)}', end=' ')
    print()