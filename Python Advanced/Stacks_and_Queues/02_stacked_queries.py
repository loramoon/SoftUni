n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    if int(command[0]) == 1:
        stack.append(int(command[1]))
    elif int(command[0]) == 2 and len(stack)>0:
        stack.pop()
    elif int(command[0]) == 3 and len(stack)>0:
        print(max(stack))
    elif int(command[0]) == 4 and len(stack)>0:
        print(min(stack))
while stack:
    if len(stack)>1:
        print(stack.pop(), end=', ')
    else:
        print(stack.pop())