import re

text = "GoshoiPeshosapochtiPichove"
pattern = '(?is)(p)'
print(re.findall(pattern, text))