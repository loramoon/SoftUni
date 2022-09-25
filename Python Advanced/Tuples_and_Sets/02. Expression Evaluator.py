from collections import deque
line = input().split()
production = deque([])
result = 0

for symbol in line:
    a = symbol.isdigit()
    if a:
        production.append(int(symbol))
    else:
        if symbol == '-' and len(production)>1:
            for el in production:
                if result == 0:
                    result = production.popleft()
                    result -= production.popleft()
                    break
                else:
                    result -= production.popleft()
                    result -= production.popleft()
                    break
        elif symbol == '*' and len(production)>0:
            for el in production:
                if result == 0:
                    result = production.popleft()
                    result *= production.popleft()
                    break
                else:
                    result *= production.popleft()
                    result *= production.popleft()
                    break
        elif symbol == '+' and len(production)>1:
            for el in production:
                if result == 0:
                    result = production.popleft()
                    result += production.popleft()
                    break
                else:
                    result += production.popleft()
                    result += production.popleft()
                    break
        elif symbol == '/':
            while production:
                if result == 0:
                    break
                else:
                    result //= production.popleft()


print(result)