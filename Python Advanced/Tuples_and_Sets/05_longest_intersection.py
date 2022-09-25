n = int(input())
count_max = -8565465465654654656
longest_intersection = []

for _ in range(n):
    set_1 = set([])
    set_2 = set([])
    first_set, second_set = input().split('-')
    a, b = [int(el) for el in first_set.split(',')]
    for index in range(a, b+1):
        set_1.add(index)
    a, b = [int(el) for el in second_set.split(',')]
    for index in range(a, b+1):
        set_2.add(index)
    intersection = set_1 & set_2
    count = sum(1 for num in intersection)
    if count>count_max:
        count_max = count
        longest_intersection = intersection
print(f"Longest intersection is {[*longest_intersection]} with length {count_max}")
