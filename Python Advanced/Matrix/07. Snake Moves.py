rows, cols = [int(el) for el in input().split()]
word = input()
idx=0

for row in range(rows):
    row_elements = []
    for col in range(cols):
        row_elements.append(word[idx % len(word)])
        idx += 1
    if row % 2 == 0:
        print(*row_elements, sep='')
    elif row % 2 != 0:
        print(*reversed(row_elements), sep='')
