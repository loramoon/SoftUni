
def get_chars(first_number, second_number):
    collected_chars = []
    for current_number in range (ord(first_number)+1, ord(second_number)):
        collected_chars.append(chr(current_number))
    return collected_chars

a = input()
b = input()
result = get_chars(a, b)
print(' '.join(result))

