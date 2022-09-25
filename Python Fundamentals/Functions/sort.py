# with list
# numbers = print(sorted(list(map(int, input().split()))))

# with function
def function(numbers):
    new_list = []
    for i in numbers:
        new_list.append(i)
    return sorted(new_list)

numbers = list(map(int, input().split()))
print(function(numbers))