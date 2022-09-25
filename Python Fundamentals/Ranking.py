contest_data = input().split(":")
data = {}
while contest_data[0] != "end of contests":
    course = contest_data[0]
    password = contest_data[1]

    data[course] = password
    contest_data = input().split(":")

user_data = input().split("=>")
user_point = {}

while user_data[0] != "end of submissions":
    course = user_data[0]
    password = user_data[1]
    user = user_data[2]
    points = int(user_data[3])
    course_points = {}
    if course in data.keys():
        if password in data.values():
            if user not in user_point.keys():
                user_point[user] = course_points
                course_points[course] = points
            elif user in user_point.keys():
                for a, b in user_point.items():
                    if user == a:
                        for k, v in b.items():
                            if k == course:
                                b[k] = max(v, points)
                                break
                            else:
                                b[course] = points
                                break

    user_data = input().split("=>")

user_point = {n: v for n, v in (sorted(user_point.items()))}
for key, value in user_point.items():
    v = {k: p for k, p in sorted(value.items(), key=lambda x: -x[1])}
    user_point[key] = v

max_points = 0
best_candidate = ''

for key, value in user_point.items():
    current_points = 0
    for sk, sv in value.items():
        current_points += sv
    if current_points > max_points:
        max_points = current_points
        best_candidate = key

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
for key, value in user_point.items():
    print(key)
    for c, p in value.items():
        print(f"#  {c} -> {p}")