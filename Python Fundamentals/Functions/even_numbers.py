numbers_as_digits = [int(s) for s in input().split()]
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)