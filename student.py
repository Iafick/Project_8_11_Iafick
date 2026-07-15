"""
Project: Student Course Registration System
Author: Imran Afick
Purpose: Contains the Student class and manages student information,
course enrollment, and grades.
Date: July,13, 2026 ## updated date
"""


class Student:
    """
    Represents a student in the registration system.

    Attributes:
        student_id (str): Unique identifier for the student.
        name (str): Student's full name.
        major (str): Student's academic major.
        courses (dict): Courses currently enrolled by the student.
    """

    def __init__(self, student_id, name, major):
        """
        Initializes a new Student object.

        Args:
            student_id (str): Unique student identifier.
            name (str): Student name.
            major (str): Student major.
        """

        self.student_id = student_id
        self.name = name
        self.major = major
        self.courses = {}


    def enroll_course(self, course):
        """
        Enrolls the student in a course.

        Args:
            course: Course object to add.
        """

        if course.course_id not in self.courses:
            self.courses[course.course_id] = {
                "name": course.name,
                "grade": None
            }


    def add_grade(self, course_id, grade):
        """
        Adds or updates a student's grade.

        Args:
            course_id (str): Course identifier.
            grade (float): Student grade.

        Raises:
            ValueError: If grade is outside the valid range.
        """

        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")

        if course_id in self.courses:
            self.courses[course_id]["grade"] = grade


    def calculate_average(self):
        """
        Calculates the student's average grade.

        Returns:
            float: Average grade.
        """

        grades = []

        for course in self.courses.values():
            if course["grade"] is not None:
                grades.append(course["grade"])

        if not grades:
            return 0

        return sum(grades) / len(grades)


    def display_info(self):
        """
        Displays student information and enrolled courses.
        """

        print("\n-------------------")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Major:", self.major)

        if self.courses:
            print("Courses:")

            for course_id, info in self.courses.items():
                print(
                    f"{course_id} - {info['name']} "
                    f"(Grade: {info['grade']})"
                )