text = input()
products = {}

while text != "statistics":
    text = text.split(": ")
    key = text[0]
    value = int(text[1])
    if key in products:
        products[key] += value
    else:
        products[key] = value
    text = input()
print("Products in stock:")
for key in products:
    print(f"- {key}: {products[key]}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
