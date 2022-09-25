# 3495892137259234

def function_even(number):
    sum_of_even = 0
    for i in str(number):
        if int(i) % 2 == 0:
            sum_of_even += int(i)
    return sum_of_even

def function_odd(number):
    sum_of_odd = 0
    for i in str(number):
        if int(i) % 2 != 0:
            sum_of_odd += int(i)
    return sum_of_odd

number = int(input())
sum_of_odd = function_odd(number)
sum_of_even = function_even(number)

print(f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}")