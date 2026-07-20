        #Method Overriding
    #A child class can replace a parent's method
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        print("Bark Bark")
dog = Dog()
dog.speak()
dog.speak()



        #Using Super()
    #super() allows the child to call the parent class construcor or methods

class person:
    def __init__(self,name):
        self.name = name
class Student(person):
    def __init__(self,name,branch):
        super().__init__(name)
        self.branch = branch
student = Student("Sai","Cyber Security")

print(student.name)
print(student.branch)


# Method overriding with inheritance for books
class Book:
    def __init__(self, title):
        self.title = title

    def info(self):
        print("Book:", self.title)


class EBook(Book):
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size

    def info(self):
        print("Book:", self.title)
        print("Size:", self.size, "MB")


class PrintedBook(Book):
    def __init__(self, title, pages):
        super().__init__(title)
        self.pages = pages

    def info(self):
        print("Book:", self.title)
        print("Pages:", self.pages)


class AudioBook(Book):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration

    def info(self):
        print("Book:", self.title)
        print("Duration:", self.duration, "minutes")


books = [
    EBook("Python OOP", 15),
    PrintedBook("Python Basics", 300),
    AudioBook("Python for Beginners", 45),
]

for book in books:
    book.info()
    print()