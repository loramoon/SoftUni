courses = {}
data_1 = input()
registered_students = {}
while True:
    if data_1 == "end":
        break
    data = data_1.split(" : ")
    course_name = data[0]
    if course_name not in registered_students.keys():
        registered_students[course_name] = 0
    registered_students[course_name] += 1
    user_name = data[1]
    courses[user_name] = course_name
    data_1 = input()

for key, value in registered_students.items():
    print(f"{key}: {value}")
    for user, course in courses.items():
        if course == key:
            print(f"-- {user}")