records = {}

while True:
    telephone = input()
    if '-' not in telephone:
        break
    name, number = telephone.split("-")
    records[name] = number
for _ in range(int(telephone)):
    contact = input()
    if contact in records:
        print(f"{contact} -> {records[contact]}")
    else:
        print(f"Contact {contact} does not exist.")

