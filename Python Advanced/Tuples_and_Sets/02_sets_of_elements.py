n, m = [int(el) for el in input().split()]
set_n = set([])
set_m = set([])

for _ in range(n):
    num1 = int(input())
    set_n.add(num1)
for _ in range(m):
    num1 = int(input())
    set_m.add(num1)

intersection = set_n & set_m
print('\n'.join(str(el) for el in intersection))