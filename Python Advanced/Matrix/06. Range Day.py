def get_next_pos(direct, row, col, step):
    if direct == 'up':
        return row-step, col
    if direct == 'down':
        return row+step, col
    if direct == 'left':
        return row, col-step
    if direct == 'right':
        return row, col+step


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size

size = 5
matrix = []

player_row = 0
player_col = 0
total_target = 0
hit_targets = []

for i in range(size):
    matrix.append([el for el in input().split()])
    for j in range(size):
        if matrix[i][j] == "A":
            player_row = i
            player_col = j
        elif matrix[i][j] == "x":
            total_target += 1

n = int(input())

for _ in range(n):
    command_args = input().split()
    command = command_args[0]
    direction = command_args[1]
    if command == 'move':
        steps = int(command_args[2])
        next_row, next_col = get_next_pos(direction, player_row, player_col, steps)

        if is_outside(next_row, next_col, size) or matrix[next_row][next_col] != '.':
            continue

        matrix[player_row][player_col] = '.'
        player_row, player_col = next_row, next_col
        matrix[player_row][player_col] = 'A'

    else:
        bullet_row, bullet_col = player_row, player_col
        while True:
            bullet_row, bullet_col = get_next_pos(direction, bullet_row, bullet_col, 1)

            if is_outside(bullet_row, bullet_col, size):
                break

            if matrix[bullet_row][bullet_col] == 'x':
                total_target -= 1
                matrix[bullet_row][bullet_col] = '.'
                hit_targets.append([bullet_row, bullet_col])
                break

        if total_target == 0:
            break

if total_target == 0:
    print(f'Training completed! All {len(hit_targets)} targets hit.')
else:
    print(f"Training not completed! {total_target} targets left.")

for hit_target in hit_targets:
    print(hit_target)
