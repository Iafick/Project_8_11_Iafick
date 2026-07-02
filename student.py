"""
Student module
Handles student data storage and operations
"""

from course import courses

students = {}


def register_student():
    """Register a new student"""

    student_id = input("Student ID: ")
    name = input("Student Name: ")
    major = input("Major: ")

    if student_id in students:
        print("Student already exists!")
        return

    students[student_id] = {
        "name": name,
        "major": major,
        "courses": {}
    }

    print("Student registered successfully!")


def display_students():
    """Display all students"""

    if not students:
        print("No students found.")
        return

    for student_id, info in students.items():
        print("\n-------------------")
        print("ID:", student_id)
        print("Name:", info["name"])
        print("Major:", info["major"])

        if info["courses"]:
            print("Courses:")
            for course_id, course_info in info["courses"].items():
                print(f"  {course_id} - {course_info['name']} (Grade: {course_info['grade']})")


def enroll_student():
    """Enroll a student in a course"""

    student_id = input("Student ID: ")
    course_id = input("Course ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    if course_id not in courses:
        print("Course not found.")
        return

    students[student_id]["courses"][course_id] = {
        "name": courses[course_id]["name"],
        "grade": None
    }

    print("Student enrolled successfully!")


def enter_grade():
    """Enter grade for a student course"""

    student_id = input("Student ID: ")
    course_id = input("Course ID: ")
    grade = input("Enter Grade (0-100): ")

    if student_id not in students:
        print("Student not found.")
        return

    if course_id not in students[student_id]["courses"]:
        print("Student not enrolled in this course.")
        return

    students[student_id]["courses"][course_id]["grade"] = float(grade)


def student_report():
    """Display full report for a student"""

    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("\n======================")
    print(" STUDENT REPORT")
    print("======================")
    print("Name:", student["name"])
    print("Major:", student["major"])

    courses_data = student["courses"]

    if not courses_data:
        print("No courses enrolled.")
        return

    total = 0
    count = 0

    print("\nCourses:")
    print("----------------------")

    for course_id, info in courses_data.items():
        grade = info["grade"]
        print(f"{course_id} - {info['name']} : {grade}")

        if grade is not None:
            total += grade
            count += 1

    if count == 0:
        print("\nNo grades available yet.")
        return

    average = total / count

    print("\n----------------------")
    print("Average:", round(average, 2))

    if average >= 90:
        print("Letter Grade: A")
    elif average >= 80:
        print("Letter Grade: B")
    elif average >= 70:
        print("Letter Grade: C")
    elif average >= 60:
        print("Letter Grade: D")
    else:
        print("Letter Grade: F")