import copy
from collections import deque

N = int(input())
total_fuel = 0
stops = 0
que = deque()

for _ in range(N):
    que.append(input())

original_que = copy.deepcopy(que)

while que:
    if stops == len(que):
        print(original_que.index(que[0]))
        break

    for position in range(N):
        fuel, distance = que[position].split()
        total_fuel += int(fuel)

        if total_fuel >= int(distance):
            total_fuel -= int(distance)
            stops += 1

        else:
            que.append(que.popleft())
            total_fuel = 0
            stops = 0
            break