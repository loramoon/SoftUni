n = int(input())
chemicals = []

for _ in range(n):
    chemical = input().split()
    chemicals.extend(chemical)

print('\n'.join(set(chemicals)))