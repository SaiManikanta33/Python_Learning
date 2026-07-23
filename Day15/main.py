from student import student
from file_handler import save_students,display_students
from utils import calculate_grade


while True:
    print("\n ====== Student Management System ======")
    print("1.Add Student")
    print("2. View Students")
    print("3. Search By Roll Number")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        roll = input("Roll Number:")
        name = input("Name: ")
        branch = input("Branch: ")
        cgpa = float(input("CGPA:   "))
        
        student1 = student(roll, name, branch, cgpa)
        
        save_students(student1)
        
        print("Grade:", calculate_grade(student1.get_cgpa()))
        
    elif choice == "2":
        display_students()
    
    elif choice == "3":
        search_query = input("Enter roll number to search:")
        result = student.search_student(search_query)
        if result:
            print("\n --- Student Details found ---")
            result.display()
            
            status = result.intern_eligibility()
            print(f"Intership Eligiblity: {status}")
        else:
            print("Not found")
    
    elif choice == "4":
        student_id= input("Enter student_id for delete:")
        res = student.delete_student(student_id)
        if res:
            print("\n ----- Student Details After deleted ------")
            res.display()
        else:
            print("Not found")
    
    elif choice == "5":
        break
    
    else:
        print("Invalid Choice")