rows = int(input())
result = []

for row in range(rows):
    nums = [int(el) for el in input().split(', ')]
    result.extend(nums)

print(result)
