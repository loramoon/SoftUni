# galia
import re

names = input().split(', ')
command = input()

expression = r'\w'
result = []
racers = []
distance = []
result_dict = {}

while command != "end of race":
    if command == "end of race":
        break
    result = re.findall(expression, command)
    racers = ''.join([ch for ch in result if ch.isalpha()])
    distance = sum([int(digit) for digit in result if digit.isdigit()])

    if racers in names and racers not in result_dict:
        result_dict[racers] = distance
    elif racers in names and racers in result_dict:
        result_dict[racers] += distance
    command = input()

i = 1
result_dict = sorted(result_dict.items(), key=lambda x: -x[1])
for k, v in result_dict:
    if i == 4:
        break
    if i == 1:
        print(f'1st place: {k}')
    elif i == 2:
        print(f'2nd place: {k}')
    elif i == 3:
        print(f'3rd place: {k}')
    i += 1
