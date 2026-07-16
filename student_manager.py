"""
Project: Student Course Registration System
Author: Imran Afick
Purpose: Manages student registration, course enrollment,
and grade operations.
Date: July 13, 2026
"""

import json

from student import Student
from course import Course


students = {}
courses = {}


def register_student(student_id, name, major):
    """
    Creates a new student and stores it in the system.

    Args:
        student_id (str): Student identifier.
        name (str): Student name.
        major (str): Student major.

    Returns:
        Student: Newly created student object.
    """

    if student_id in students:
        raise ValueError("Student already exists.")

    new_student = Student(
        student_id,
        name,
        major
    )

    students[student_id] = new_student

    return new_student



def add_course(course_id, name, credits):
    """
    Creates and stores a new course.

    Args:
        course_id (str): Course identifier.
        name (str): Course name.
        credits (int): Credit hours.

    Returns:
        Course: Newly created course object.
    """

    if course_id in courses:
        raise ValueError("Course already exists.")

    new_course = Course(
        course_id,
        name,
        credits
    )

    courses[course_id] = new_course

    return new_course



def enroll_student(student_id, course_id):
    """
    Enrolls a student into a course.

    Args:
        student_id (str): Student identifier.
        course_id (str): Course identifier.
    """

    if student_id not in students:
        raise ValueError("Student does not exist.")

    if course_id not in courses:
        raise ValueError("Course does not exist.")

    students[student_id].enroll_course(
        courses[course_id]
    )



def add_grade(student_id, course_id, grade):
    """
    Adds a grade to a student's course.

    Args:
        student_id (str): Student identifier.
        course_id (str): Course identifier.
        grade (float): Grade value.
    """

    if student_id not in students:
        raise ValueError("Student does not exist.")

    students[student_id].add_grade(
        course_id,
        grade
    )



def save_students():
    """
    Saves student information into a JSON file.
    """

    student_data = []

    for student in students.values():

        student_data.append({
            "student_id": student.student_id,
            "name": student.name,
            "major": student.major,
            "courses": student.courses
        })

    with open("students.json", "w") as file:
        json.dump(
            student_data,
            file,
            indent=4
        )



def load_students():
    """
    Loads student information from a JSON file.

    Handles missing files without crashing.
    """

    try:

        with open("students.json", "r") as file:
            student_data = json.load(file)


            for data in student_data:

                student = Student(
                    data["student_id"],
                    data["name"],
                    data["major"]
                )

                student.courses = data["courses"]

                students[student.student_id] = student


    except FileNotFoundError:

        print("No saved student data found.")



def display_students():
    """
    Displays all students in the system.
    """

    if not students:
        print("No students registered.")

        return

    for student in students.values():
        student.display_info()



def display_courses():
    """
    Displays all available courses.
    """

    if not courses:
        print("No courses available.")

        return

    for course in courses.values():
        course.display_info()