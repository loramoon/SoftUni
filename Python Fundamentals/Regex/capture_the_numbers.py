import re
numbers = input()
search_pattern = r"\d+"
all_numbers = []

while numbers:
    result = re.findall(search_pattern, numbers)
    all_numbers.extend(result)
    numbers = input()

print(' '.join(all_numbers))
