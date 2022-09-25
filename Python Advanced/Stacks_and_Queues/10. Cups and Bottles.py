from collections import deque

cup = deque([int(x) for x in input().split()])
bottle = [int(x) for x in input().split()]
wasted_water = 0

while cup and bottle:
    c = cup.popleft()
    b = bottle.pop()
    if c == b:
        pass
    elif c < b:
        wasted_water += b-c
    elif c > b:
        c -= b
        cup.insert(0, c)

if not cup:
    print(f"Bottles:", ' '.join(str(el) for el in bottle))
if not bottle:
    print(f"Cups:", ' '.join(str(el) for el in cup))
print(f'Wasted litters of water: {wasted_water}')