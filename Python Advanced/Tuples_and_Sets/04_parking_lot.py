n = int(input())
parking = set([])

for _ in range(n):
    command, plate = input().split(', ')
    if command == "IN":
        parking.add(plate)
    elif command == "OUT":
        if plate in parking:
            parking.remove(plate)

if len(parking) == 0:
    print("Parking Lot is Empty")
else:
    print('\n'.join(parking))