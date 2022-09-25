
def calculation(type):
    result = None
    if type == "multiply":
        result = a * b
    elif type == "divide":
        result = a / b
    elif type == "add":
        result = a + b
    elif type == "subtract":
        result = a - b
    return result
type = input()
a = int(input())
b = int(input())

print(int(calculation(type)))