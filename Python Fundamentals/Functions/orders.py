def order(product, quantity):
    price = 0
    if product=='coffee':
        price = 1.5
    elif product == 'water':
        price = 1
    elif product == 'coke':
        price = 1.40
    elif product == 'snacks':
        price = 2
    return f'{price*quantity:.2f}'

product = input()
quantity = int(input())
print(order(product, quantity))

