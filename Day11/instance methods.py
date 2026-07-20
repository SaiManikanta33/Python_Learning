        #Instance methods
    #instance methods work with objects-specific data
class Student:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hello, I am {self.name}")
student = Student("Sai")
student.greet()