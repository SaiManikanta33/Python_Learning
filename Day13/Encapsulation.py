        #Encapsulation
    #Encapsulation protects an object data by controlling access
    
#Public Attribute

class Student:
    def __init__(self):
        self.name  = "Sai"
student = Student()
print(student.name)

#Protected Attribute
#(Converts prefix with _)

class Student:
    def __init__(self):
        self._branch="Cyber Security"
student = Student()
print(student._branch)

#Private Attribute
#(name mangling with _)

"""class BankAccount:
    def __init__(self):
        self.__balance = 5000
acc = BankAccount()
print(acc.__balance)"""         #Here Comes Error because can't access priate variable data



#Access Through methods:
class BankAccount:
    def __init__(self):
        self.__balance = 5000
    def get_balance(self):
        return self.__balance
acc = BankAccount()
print(acc.get_balance())
