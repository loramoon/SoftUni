parentheses = input()
open = []
balanced = True
for ch in parentheses:
    if ch in "([{":
        open.append(ch)
    elif ch in ")]}" and len(open) == 0:
        print("NO")
        exit()
    else:
        if len(open)>0:
            last_bracket = open.pop()
            if f'{last_bracket}{ch}' not in "()[]{}":
                balanced = False
                break
if balanced and not open:
    print('YES')
else:
    print("NO")

