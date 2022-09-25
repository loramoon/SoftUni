clothes_stack = [int(el) for el in input().split()]
rack_capacity = int(input())
current_rack = rack_capacity
number_rack = 1

while clothes_stack:
    current_cloth = clothes_stack[-1]
    if current_cloth <= current_rack:
        current_rack -= current_cloth
        clothes_stack.pop()
    else:
        number_rack +=1
        current_rack = rack_capacity
        current_rack -= current_cloth
        clothes_stack.pop()
print(number_rack)