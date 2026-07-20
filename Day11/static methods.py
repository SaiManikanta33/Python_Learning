            #Static methods
    #Static methods don't use self or cls .they are utility functions relates to the class
class calculator:
    @staticmethod
    def add(a,b):
        return a+b
print(calculator.add(3,5))