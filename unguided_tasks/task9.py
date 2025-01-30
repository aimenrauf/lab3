def store_and_sort_grades():
    students = []
    for i in range(5):
        name = input(f"Enter the name of student {i + 1}: ")
        grade = float(input(f"Enter the grade for {name}: "))
        students.append((name, grade))
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    print("\nSorted Grades (Descending Order):")
    for student in sorted_students:
        print(f"{student[0]}: {student[1]}")
store_and_sort_grades()