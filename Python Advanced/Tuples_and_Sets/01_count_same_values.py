nums = (float(el) for el in input().split())
occ = {}

for num in nums:
    if num not in occ:
        occ[num] = 0
    occ[num] += 1

for data in occ.items():
    print(f"{data[0]} - {data[1]} times")