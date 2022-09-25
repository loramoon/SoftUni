import sys

def function_min_max(numbers):
    min_number = sys.maxsize
    max_number = -sys.maxsize
    sum_numbers = 0
    for i in numbers:
        sum_numbers += int(i)
        if int(i)>max_number:
            max_number=int(i)
        if int(i)<min_number:
            min_number=int(i)
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_numbers}")

numbers = input().split()
function_min_max(numbers)