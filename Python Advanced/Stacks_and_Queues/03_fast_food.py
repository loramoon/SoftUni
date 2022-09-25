from collections import deque
quantity_food = int(input())

orders_queue = deque(map(int, input().split()))

max_order = max(orders_queue)
print(f"{max_order}")

while orders_queue:
    current_order = orders_queue[0]
    if current_order <= quantity_food:
        quantity_food -= orders_queue.popleft()
    else:
        break
if orders_queue:
    print(f"Orders left: {' '.join(str(el) for el in orders_queue)}")
else:
    print('Orders complete')