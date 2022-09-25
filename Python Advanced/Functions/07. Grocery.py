def grocery_store(**kwargs):
    sorted_list = [f'{key}: {value}' for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
    return '\n'.join(sorted_list)


print(grocery_store(
    bread=20,
    аasta=20,
    eggs=20,
    carrot=1,
))
