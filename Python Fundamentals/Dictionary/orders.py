command = input()
products = {}
prices = {}

while command != "buy":
    items = command.split(' ')
    for i in range(0, len(items), 3):
        item = items[0]
        price = float(items[1])
        quantity = int(items[2])
        if item not in products.keys():
            products[item] = 0
        products[item] += quantity
        prices[item] = price
    command = input()

for item, quantity in products.items():
    total = quantity * prices[item]
    print(f"{item} -> {total:.2f}")
