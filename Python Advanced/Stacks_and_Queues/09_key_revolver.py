from collections import deque
price = int(input())
gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
barrel = gun_barrel

while locks and bullets:
    l = locks.popleft()
    b = bullets.pop()
    intelligence -= price
    barrel -= 1
    if b <= l:
        print('Bang!')
    else:
        print("Ping!")
        locks.insert(0, l)
    if barrel == 0 and len(bullets) != 0:
        print("Reloading!")
        barrel = gun_barrel

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
