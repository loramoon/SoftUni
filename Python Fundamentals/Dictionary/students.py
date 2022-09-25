# name_id = []
# my_students = {}
# while True:
#     students = input().split(':')
#     if len(students) == 1:
#         break
#     else:
#         name_id.append(students[0])
#         name_id.append(students[1])
#         name_id.append(students[2])
#
# for i in range (0, len(name_id), 3):
#     name = name_id[i]
#     id = name_id[i+1]
#     course = name_id[i+2]
#     course = course.replace(" ", "_")
#     if students[0] == course:
#         my_students[name] = int(id)
#
# for key, value in my_students.items():
#     print(f"{key} - {value}")

text = input()
courses = {}
data = []
while ":" in text:
    data = text.split(":")
    name = data[0]
    id = data[1]
    course = data[2]
    # (name, id, course) = text.split(":")
    if course not in courses.keys():
        courses[course] = {}
    courses[course][id] = name
    text = input()
test = text.replace("_", " ")
for id in courses[text]:
    print(f"{courses[text][id]} - {id}")
