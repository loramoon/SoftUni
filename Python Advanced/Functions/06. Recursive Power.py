def recursive_power(n, p):
    result = 1
    if p == 0:
        return result
    result = n * recursive_power(n, p-1)
    return result


print(recursive_power(2, 10))
print(recursive_power(10, 100))
