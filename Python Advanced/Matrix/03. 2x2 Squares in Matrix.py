rows, cols = [int(el) for el in input().split()]
matrix = []
count = 0
for row in range(rows):
    matrix.append([el for el in input().split()])

for row in range(rows-1):
    for col in range(cols-1):
        if matrix[row][col] == matrix[row+1][col+1] == matrix[row][col+1] == matrix[row+1][col]:
            count +=1
print(count)