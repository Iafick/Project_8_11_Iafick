"""
Project: Student Course Registration System
Author: Imran Afick
Purpose: Defines the Course class used to create and manage courses.
Date: July 2026
"""


class Course:
    """
    Represents a college course.

    Attributes:
        course_id (str): Unique identifier for the course.
        name (str): Course name.
        credits (int): Number of credit hours.
    """

    def __init__(self, course_id, name, credits):
        """
        Initializes a Course object.

        Args:
            course_id (str): Course identifier.
            name (str): Course name.
            credits (int): Credit hours.
        """

        self.course_id = course_id
        self.name = name
        self.credits = credits


    def display_info(self):
        """
        Displays course information.
        """

        print("\n-------------------")
        print("Course ID:", self.course_id)
        print("Name:", self.name)
        print("Credits:", self.credits)