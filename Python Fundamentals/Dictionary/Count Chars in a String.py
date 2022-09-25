# letter_dict = {}
# text = ''.join(x for x in input().split())
# for letter in text:
#     if letter not in letter_dict:
#         letter_dict[letter] = 0
#     letter_dict[letter] += 1
# for key, value in letter_dict.items():
#     print(f"{key} -> {value}")

from collections import Counter
word = input()
result = Counter(word)
for key, value in result.items():
    if key != " ":
        print(f"{key} -> {value}")
