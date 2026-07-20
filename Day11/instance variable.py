        #Instance variables
    #instance variables belong to each object individually
class Student:
    def __init__(self,name,branch):
        self.name = name
        self.branch=branch
student1  = Student("Sai","Cyber Securiy")
student2 = Student("Mani","Cyber")

print(student1.name)
print(student2.name)
print(student2.branch)
    #Each object stores its own values
    
    