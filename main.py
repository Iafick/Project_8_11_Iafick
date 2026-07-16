"""
Project: Student Course Registration System
Author: Imran Afick
Purpose: A student management system demonstrating functions,
object-oriented programming, file I/O, JSON persistence,
exception handling, and automated testing.
Date: July, 2026
"""

from tokenize import String

from student_manager import (
    register_student,
    display_students,
    enroll_student,
    add_grade,
    add_course,
    display_courses
)


def display_menu():
    """
    Displays the available options for the Student Management System.
    """

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
    """
    Runs the main program loop and handles user choices.
    """

    while True:
        display_menu()

        try:
            choice = input("Choose an option: ")

            if choice == "1":
                student_id = input("Student ID: ")
                name = input("Student Name: ")
                major = input("Major: ")

                register_student(
                    student_id,
                    name,
                    major
                )

                print("Student registered successfully!")


            elif choice == "2":
                display_students()


            elif choice == "3":
                student_id = input("Student ID: ")
                course_id = input("Course ID: ")

                enroll_student(
                    student_id,
                    course_id
                )

                print("Student enrolled successfully!")


            elif choice == "4":
                student_id = input("Student ID: ")
                course_id = input("Course ID: ")
                grade = float(input("Enter Grade (0-100): "))

                add_grade(
                    student_id,
                    course_id,
                    grade
                )

                print("Grade added successfully!")


            elif choice == "5":
                course_id = input("Course ID: ")
                name = input("Course Name: ")
                credits = int(input("Credits: "))

                add_course(
                    course_id,
                    name,
                    credits
                )

                print("Course added successfully!")


            elif choice == "6":
                display_courses()


            elif choice == "7":
                print("Goodbye!")
                break


            else:
                print("Invalid option. Please select 1-7.")


        except ValueError as error:
            print(f"Invalid input: {error}")


        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            


if __name__ == "__main__":
    main()
    # Program finished
          
    
        