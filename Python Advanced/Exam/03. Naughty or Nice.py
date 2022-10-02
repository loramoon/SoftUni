def naughty_or_nice_list(*args, **kwargs):
    santa_list = {'Nice': [], 'Naughty': [], 'Not found': []}
    all_kids = {}
    for number, name in args[0]:
        if number not in all_kids.keys():
            all_kids[number] = []
        all_kids[number].append(name)
    for tuple_ in args[1:]:
        num, list_name = tuple_.split('-')
        num = int(num)
        if num in all_kids.keys() and len(all_kids[num]) == 1:
            santa_list[list_name].extend(all_kids[num])
            del all_kids[num]

    for code, kid in kwargs.items():
        if kid in santa_list.keys():
            for num, name in all_kids.items():
                if code in name:
                    santa_list[kid].extend([code])
                    all_kids[num].remove(code)

    if len(all_kids) > 0:
        for kid in all_kids.values():
            santa_list["Not found"].extend(kid)

    final_result = ''
    for code, kid in santa_list.items():
        if len(kid) > 0:
            final_result += f"{code}: {', '.join(kid)}\n"
    return final_result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
