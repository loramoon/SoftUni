n = int(input())
students = {}
grades = {}

for i in range(n):
    student_name = input()

    if student_name not in students:
        grade = float(input())
        grades[student_name] = 1
        students[student_name] = grade
    else:
        students[student_name] = students.get(student_name, 0) + float(input())
        grades[student_name] += 1

for key, value in students.items():
    grade = value/grades[key]
    if grade >= 4.5:
        print(f"{key} -> {grade:.2f}")