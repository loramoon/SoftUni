def words_sorting(*args):
    list_ = {}
    total = 0
    for i in args:
        char_sum = 0
        for char in i:
            char_sum += ord(char)
        result = char_sum
        total += result
        list_[i] = result

    if total % 2 != 0:
        sorted_list = sorted(list_.items(), key=lambda x: (-(x[1])))
    else:
        sorted_list = sorted(list_.items(), key=lambda x: (x[0]))

    final = ''
    for k, v in sorted_list:
        final += f"{k} - {v}\n"

    return final

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

