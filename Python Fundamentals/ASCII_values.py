chars = input().split(", ")

my_dict = {key: ord(key) for key in chars}

print(my_dict)
