        #Creating your first class
class student:
    print("This is Class Creation")
    pass
student = student()
print(student)


        #Attributes
class student:
    pass
student1 = student()
student1.name="Sai"
student1.age=19
student1.branch="CSC"

print(student1.name)
print(student1.age)
print(student1.branch)


        #Methods
class student:
    def introduce(self):
        print("Hello , I am a cyber security student.")
student3 = student()
print(student)


        #Contructors
class student:
    def __init__(self,name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch
student0 = student("Sai",19,"Cyber Security")
print(student0.name)
print(student0.age)
print(student0.branch)

    #example
class laptop:
    def __init__(self,brand,ram):
        self.brand = brand
        self.ram = ram
    def details(self):
        print(f"{self.brand} Laptop - {self.ram} GB RAM")
lap = laptop("Hp",16)
lap.details()


            #creating mutiple objetcs
class student:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hello {self.name}")
s1 = student("Sai")
s2 = student("Mani")
s3 = student("Pavan")

s1.greet()
s2.greet()
s3.greet()