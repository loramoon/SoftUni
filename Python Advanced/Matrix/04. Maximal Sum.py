rows, cols = [int(el) for el in input().split()]
matrix = []
max_sum = -987987999999999
max_matrix = []
cur_sum = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split()])

for row in range(rows-2):
    for col in range(cols-2):
        cur_matrix = [matrix[row][col], matrix[row+1][col], matrix[row+2][col], matrix[row][col+1], matrix[row+1][col+1], matrix[row+2][col+1], matrix[row][col+2], matrix[row+1][col+2], matrix[row+2][col+2]]
        matrix_sum = sum(cur_matrix)
        if matrix_sum>max_sum:
            max_sum = matrix_sum
            max_matrix = cur_matrix.copy()
print(f"Sum = {max_sum}")
print(max_matrix[0],max_matrix[3], max_matrix[6])
print(max_matrix[1],max_matrix[4], max_matrix[7])
print(max_matrix[2],max_matrix[5], max_matrix[8])