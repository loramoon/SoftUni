import re

tel_numbers = input()

search_pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

result = re.findall(search_pattern, tel_numbers)

print(', '.join(result))
