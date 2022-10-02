def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    basket = {}
    for product, values in kwargs.items():
        price, quantity = values
        sub_total = quantity*price
        if sub_total <= budget:
            basket[product] = sub_total
            budget -= sub_total
            if len(basket) == 5 or budget == 0:
                break
    final_result = ''
    for product, subtotal in basket.items():
        if subtotal:
            final_result += f"You bought {product} for {subtotal:.2f} leva.\n"

    return final_result

print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
