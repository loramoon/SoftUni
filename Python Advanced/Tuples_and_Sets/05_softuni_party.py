n = int(input())
regular = set()

for _ in range(n):
    reservation_code = input()
    regular.add(reservation_code)

guest = input()
while guest != "END":
    if guest in regular:
        regular.remove(guest)
    guest = input()

print(f"{len(regular)}")

if regular:
    print('\n'.join(sorted(regular)))