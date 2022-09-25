

def absolute_name(numbers):
    result = [abs(num) for num in numbers]
    return result

numbers = list(map(float, input().split()))
print(absolute_name(numbers))