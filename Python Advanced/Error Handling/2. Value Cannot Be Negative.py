class ValueCannotBeNegative(Exception):
    """"Number is below zero"""


for i in range(5):
    numbers = int(input())
    if numbers < 0:
        raise ValueCannotBeNegative
