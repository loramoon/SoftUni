n = int(input())
matrix = []
primer_diagonal_sum = 0
second_diagonal_sum = 0

for row in range(n):
    matrix.append([int(el) for el in input().split()])

for row in range(n):
    for col in range(n):
        if row == col:
            primer_diagonal_sum += matrix[row][col]
            second_diagonal_sum += matrix[row][n-1-col]
print(abs(primer_diagonal_sum-second_diagonal_sum))


