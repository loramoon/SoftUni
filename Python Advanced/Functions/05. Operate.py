def operate(operation, *args):
    def add(*args):
        return sum(y for y in args)
    def subtract(x, *args):
        return x - sum(y for y in args)
    def multiply(*args):
        result = 1
        for values in args:
            result *= values
        return result
    def divide(x, *args):
        result = x
        for values in args:
            result /= values
        return result
    if operation == '+':
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    elif operation == '/':
        return divide(*args)
    else:
        return None



print(operate("-", 10, 5, 3))
print(operate("-", 3, 4))
