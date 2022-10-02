def shopping_cart(*args):
    cart = {'Pizza': [], 'Soup': [], 'Dessert': []}
    for i in args:
        if i == 'Stop':
            break
        meal = i[0]
        product = i[1]

        if meal == 'Pizza' and len(cart['Pizza']) == 4:
            continue
        elif meal == 'Soup' and len(cart['Soup']) == 3:
            continue
        elif meal == 'Dessert' and len(cart['Dessert']) == 2:
            continue
        if product not in cart[meal]:
            cart[meal].append(product)

    for value in cart.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_cart = sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for i in sorted_cart:
        result += f"{i[0]}:\n"
        sorted_product = sorted(i[1])
        for product in sorted_product:
            result += f" - {product}\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
