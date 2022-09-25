from collections import deque


def get_index(bomb):
    start = bomb - 1
    if start < 0:
        start = 0
    end = bomb + 1
    if end > n - 1:
        end = n - 1
    return start, end


n = int(input())
matrix = []
alive = 0
alive_sum = 0

for i in range(n):
    matrix.append([int(x) for x in input().split()])

bombs = deque(input().split())


while bombs:
    b_row, b_col = eval(bombs.popleft())
    if matrix[b_row][b_col] > 0:
        energy = matrix[b_row][b_col]

        start_row_idx, end_row_idx = get_index(b_row)
        start_col_idx, end_col_idx = get_index(b_col)

        for row in range(start_row_idx, end_row_idx + 1):
            for col in range(start_col_idx, end_col_idx + 1):
                if matrix[row][col] > 0:
                    matrix[row][col] -= energy

for i in range(n):
    for j in range(n):
        if matrix[i][j]>0:
            alive += 1
            alive_sum += matrix[i][j]

print(f"Alive cells: {alive}")
print(f"Sum: {alive_sum}")
for i in matrix:
    print(*i)
