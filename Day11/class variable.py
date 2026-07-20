        #Class variables
    #A class variables is shared by all objects
class Student:
    college = "Raghu Engeneering College"
    
    def __init__(self,name):
        self.name = name
s1 = Student("sai")
s2 = Student("Mani")

print(s1.college)
print(s2.college)
print(s1.name)
    #if the college changes
Student.college = "ABC University"

print(s1.college)
print(s2.college)
    #Both objects now show the updated value