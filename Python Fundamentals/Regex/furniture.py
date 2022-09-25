import re
bought_furniture = []
total_cost = 0
pattern = r''
command = input()
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.group()
        bought_furniture.append(furniture)
        total_cost += int(quantity) * float(price)

    command = input()
print("Bought furniture:")
print('\n'.join(bought_furniture))
print(f"Total money spend: {total_cost:.2f}")

import re

data = input()
total_sum = []
total_products = []
while not data == 'Purchase':
    pattern = r'(\>{2})([A-Za-z]+)(\<{2})(\d+\.?\d+)(\!)(\d+)'
    result = re.finditer(pattern, data)
    for el in result:
        product = el[2]
        price = float(el[4])
        count = int(el[6])
        total_products.append(product)
        total_sum.append(price * count)

    data = input()

print("Bought furniture:")
for product in total_products:
    print(product)
print(f"Total money spend: {sum(total_sum):.2f}")
