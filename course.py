"""
Course module
Handles course creation and storage
"""

courses = {}


def add_course():
    """Add a new course"""

    course_id = input("Course ID (e.g. CSCI101): ")
    name = input("Course Name: ")
    credits = input("Credits: ")

    if course_id in courses:
        print("Course already exists!")
        return

    courses[course_id] = {
        "name": name,
        "credits": credits
    }

    print("Course added successfully!")


def display_courses():
    """Display all courses"""

    if not courses:
        print("No courses available.")
        return

    for course_id, info in courses.items():
        print("\n-------------------")
        print("Course ID:", course_id)
        print("Name:", info["name"])
        print("Credits:", info["credits"])