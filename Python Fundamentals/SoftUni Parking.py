n = int(input())
parking = {}

for i in range(n):
    user_data = input().split()
    command = user_data[0]
    user = user_data[1]
    if command == "register":
        plate = user_data[2]
        if user not in parking:
            parking[user] = plate
            print(f"{user} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    else:
        if user not in parking:
            print(f"ERROR: user {user} not found")
        else:
            del parking[user]
            print(f"{user} unregistered successfully")
for key, value in parking.items():
    print(f"{key} => {value}")