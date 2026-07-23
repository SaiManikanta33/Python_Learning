
import csv
import os

class student:
    def __init__(self, roll_no, name, branch, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.branch = branch
        self.__cgpa = cgpa

    def display(self):
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Branch  : {self.branch}")
        print(f"CGPA    : {self.__cgpa}")

    def get_cgpa(self):
        return self.__cgpa

    def set_cgpa(self, cgpa):
        if 0 <= cgpa <= 10:
            self.__cgpa = cgpa

    def intern_eligibility(self):
        if self.__cgpa >= 7.5:
            return f"{self.name} Eligible For Intership"
        else:
            return "Not Eligible (Requires minimum 7.5 CGPA)"
        
    @staticmethod
    def search_student(target_roll):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(base_dir, "students.csv")

        try:
            with open(data_file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["roll_no"] == str(target_roll):
                        return student(row["roll_no"], row["name"], row["branch"], float(row["cgpa"]))
        except FileNotFoundError:
            print("Error: 'students.csv' file not found.")
        return None
    @staticmethod
    def delete_student(student_id):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(base_dir, "students.csv")

        deleted_student = None
        remaining_students = []

        try:
            # 1. Read all existing students
            with open(data_file, "r", newline="") as file:
                reader = csv.DictReader(file)
                fieldnames = reader.fieldnames
                for row in reader:
                    if row["roll_no"] == str(student_id):
                        deleted_student = student(
                            row["roll_no"],
                            row["name"],
                            row["branch"],
                            float(row["cgpa"]),
                        )
                    else:
                        remaining_students.append(row)

            if not deleted_student:
                return None

            # 2. Rewrite the file without the deleted student
            with open(data_file, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(remaining_students)

            print(f"Success: Student with Roll No {student_id} removed.")
            return deleted_student

        except FileNotFoundError:
            print("Error: 'students.csv' file not found.")
            return None
    