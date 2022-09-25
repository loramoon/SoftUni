def multiply(*args):
    mul = 1
    for i in args:
        mul *= int(i)
    return mul


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
