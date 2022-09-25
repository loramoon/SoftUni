matrix = input().split('|')
flat_list = []

for el in range(len(matrix)-1, -1, -1):
    cur_el = (matrix[el].strip().split())
    flat_list.extend(cur_el)

print(*flat_list)