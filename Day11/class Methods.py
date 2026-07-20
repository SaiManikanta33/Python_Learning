            #Class Methods
    #class methods work with class variables
class Student:
    college = "Raghu Engineering College"
    
    @classmethod
    def change_college(cls,new_name):
        cls.college = new_name
Student.change_college("Cyber University")
print(Student.college)
    #cls refers to the class itself