n = int(input())
A = 0
B = 0
even_set = set([])
odd_set = set([])
for index in range(n):
    name = input()

    sum_name = 0
    for ch in name:
        sum_name += ord(ch)
    dev = sum_name//(index+1)
    if dev % 2 == 0:
        even_set.add(dev)
    else:
        odd_set.add(dev)

if even_set:
    A = sum(even_set)
if odd_set:
    B = sum(odd_set)
if A == B:
    print (', '.join(str(el) for el in odd_set | even_set))
if B>A:
    print (', '.join(str(el) for el in odd_set - even_set))
if A>B:
    print (', '.join(str(el) for el in odd_set ^ even_set))