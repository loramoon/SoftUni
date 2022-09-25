students = {}
stu_list = input().split("-")
all_languages = []
count_languages = []
while stu_list[0] != "exam finished":
    if len(stu_list)>2:
        username, language, points = stu_list[0:]
        points = int(points)
        if username in students:
            if language == students[username]['language']:
                points = max(points, students[username]['points'])
        students[username] = {'language': language, 'points': points}
        all_languages.append(language)
        if language not in count_languages:
            count_languages.append(language)
    elif len(stu_list) == 2:
        username, banned = stu_list[0:]
        del students[username]

    stu_list = input().split("-")

print(f"Results:")
for username, v in students.items():
    print(f"{username} | {v['points']}")

print('Submissions:')
for i in range(len(count_languages)):
    result = count_languages[i]
    print(f"{count_languages[i]} - {all_languages.count(result)}")