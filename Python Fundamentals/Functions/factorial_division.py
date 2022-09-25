''''Write a function that receives two integer numbers. Calculate the factorial of each number.
Divide the first result by the second and print the division formatted to the second decimal point.'''

def factorial(number):
    for i in range(1, number):
        number *= i
    return number

first = int(input())
second = int(input())
first = factorial(first)
second = factorial(second)
print(f'{first/second:.2f}')