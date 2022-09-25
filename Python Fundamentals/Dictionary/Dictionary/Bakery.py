elements = input().split(' ')
my_dict = {}

for i in range (0, len(elements), 2):
    key = elements[i]
    value = elements[i+1]
    my_dict[key] = int(value)

print(my_dict)
