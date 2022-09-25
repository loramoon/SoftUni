
def sum_numbers(first, second):
    return first+second

def subtract(sum_numbers, third):
    return sum_numbers - third

def add_and_subtract(first, second, third):
    sum_numbers_int = sum_numbers(first, second)
    result = subtract(sum_numbers_int, third)
    return result

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
