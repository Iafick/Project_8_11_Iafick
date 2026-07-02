"""
Program Name: Student Grade Tracker
Author: Imran Afick
Purpose: Store students and grades and calculate averages.
Starter Code: None
Date: 06/25/2026
"""

students = {}

while True:
    print("\nStudent Grade Tracker")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Students")
    print("4. Calculate Average")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ").strip().lower()

        if name not in students:
            students[name] = []
            print("Student added.")
        else:
            print("Student already exists.")

    elif choice == "2":
        name = input("Enter student name: ").strip().lower()

        if name in students:
            grade = float(input("Enter grade: "))
            students[name].append(grade)
            print("Grade added.")
        else:
            print("Student not found.")

    elif choice == "3":
        if len(students) == 0:
            print("No students found.")
        else:
            for name, grades in students.items():
                print(name.title(), "->", grades)

    elif choice == "4":
        name = input("Enter student name: ").strip().lower()

        if name in students and len(students[name]) > 0:
            average = sum(students[name]) / len(students[name])
            print(name.title(), "average:", average)
        else:
            print("Student not found or no grades available.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Name already exists. Try again.")# If name is repeated regardless of the case either uppercase or lowwer case as long as spelling is the same.
   
    