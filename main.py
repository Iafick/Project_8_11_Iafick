"""
Project: Student Course Registration System
Author: Imran Afick
Purpose: Demonstrates Python Crash Course Chapters 1–7 concepts
Date: July 2026
"""

from student import register_student, display_students, enroll_student, enter_grade
from course import add_course, display_courses

def display_menu():
    print("\n==============================")
    print(" Student Management System")
    print("==============================")
    print("1. Register Student")
    print("2. View All Students")
    print("3. Enroll Student in Course")
    print("4. Enter Grade")
    print("5. Add Course")
    print("6. View All Courses")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            enroll_student()

        elif choice == "4":
            enter_grade()

        elif choice == "5":
            add_course()

        elif choice == "6":
            display_courses()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")
            main()