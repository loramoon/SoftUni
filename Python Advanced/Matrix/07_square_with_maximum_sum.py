rows, cols = [int(el) for el in input().split(', ')]
matrix = []
max_sub_matrix = -9999999999999
max_matrix = []
for row in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

for row in range(rows-1):
    for col in range(cols-1):
        sub_matrix = [matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]]
        current_sum = sum(sub_matrix)
        if current_sum>max_sub_matrix:
            max_sub_matrix=current_sum
            max_matrix=sub_matrix.copy()

print(max_matrix[0], max_matrix[1])
print(max_matrix[2], max_matrix[3])
print(max_sub_matrix)
