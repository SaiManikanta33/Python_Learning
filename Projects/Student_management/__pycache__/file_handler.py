
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "students.csv")


def save_students(student_obj):
    with open(DATA_FILE, "a") as file:
        file.write(
            f"{student_obj.roll_no},"
            f"{student_obj.name},"
            f"{student_obj.branch},"
            f"{student_obj.get_cgpa()}\n"
        )


def display_students():
    try:
        with open(DATA_FILE, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No students records found.")