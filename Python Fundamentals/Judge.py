user_data = input().split("->")
user_point = {}

while user_data[0] != "no more time":
    username = user_data[0]
    contest = user_data[1]
    points = int(user_data[2])
    course_points = {}
    if username not in user_point.keys():
        user_point[username] = course_points
        course_points[contest] = points
    elif username in user_point.keys():
        for a, b in user_point.items():
            if username == a:
                for k, v in b.items():
                    if k == contest:
                        b[k] = max(v, points)
                        break
                    else:
                        b[contest] = points
                        break

    user_data = input().split("->")

print(user_point)

# for key, value in user_point.items():
#     print(f""{constest_name}: {number_participants} participants")
#     for c, p in value.items():
#         print(f"#  {c} -> {p}")
