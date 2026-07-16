"""
Project: Student Course Registration System Tests
Author: Imran Afick
Purpose: Tests Student class functionality.
Date: July 15, 2026
"""

import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """
    Tests the Student class methods.
    """

    def test_student_creation(self):
        """
        Tests that a student object is created correctly.
        """

        student = Student("001", "Imran Afick", "Computer Science")

        self.assertEqual(student.student_id, "001")
        self.assertEqual(student.name, "Imran Afick")
        self.assertEqual(student.major, "Computer Science")


    def test_add_grade(self):
        """
        Tests adding grades and calculating averages.
        """

        student = Student("001", "Imran Afick", "Computer Science")

        student.courses["CS101"] = {
            "name": "Python",
            "grade": None
        }

        student.add_grade("CS101", 90)

        self.assertEqual(
            student.courses["CS101"]["grade"],
            90
        )


    def test_invalid_grade(self):
        """
        Tests that invalid grades raise errors.
        """

        student = Student("001", "Imran Afick", "Computer Science")

        with self.assertRaises(ValueError):
            student.add_grade("CS101", 120)


    def test_average_calculation(self):
        """
        Tests calculating the student's average grade.
        """

        student = Student("001", "Imran Afick", "Computer Science")

        student.courses = {
            "CS101": {
                "name": "Python",
                "grade": 80
            },
            "CS102": {
                "name": "Java",
                "grade": 100
            }
        }

        average = student.calculate_average()

        self.assertEqual(average, 90)


if __name__ == "__main__":
    unittest.main()