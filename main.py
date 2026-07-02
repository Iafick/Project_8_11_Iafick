"""
Project: Student Course Registration System

Author: Imran Afick

Purpose:
Final Project for Python Crash Course Chapters 1-7

Resources:
Python Crash Course textbook

Date:
July 1, 2026
"""
def display_menu():
    print("\n============================")
    print(" Student Management System")
    print("============================")
    print("1. Register Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Enter Grade")
    print("5. Student Report")
    print("6. View All Students")
    print("7. Search Student")
    print("8. Exit")
    
    def main():
        while True:
            display_menu()
            choice = input("Choose an option: ")
            if choice == "8":
                print("Goodbye!")
                break
            else:
                print("Feature coming soon.")
                