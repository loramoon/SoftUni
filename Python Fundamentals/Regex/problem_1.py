import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# y = re.findall("ai", txt)
# print(x)
# print(y)

names = input()
search_pattern = r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b'
result = re.findall(search_pattern, names)
print(' '.join(result))
