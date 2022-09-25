import re
text = input()
word = input()
pattern = fr'\b{word}\b'
matches = re.findall(pattern, text, flags = re.IGNORECASE)
print(len(matches))
