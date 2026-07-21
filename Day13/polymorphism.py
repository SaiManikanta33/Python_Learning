        #Pholymorphism
    #Polymorphism means "Many froms" different objects can use the same method name but perform different actions

class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
animals= [Dog(),Cat()]

for animal in animals:
    animal.sound()
    
    
    #Example 2

class PDFReport:
    def export(self):
        print("Exporting PDF")
class ExcelReport:
    def export(self):
        print("Exporting Excel")
reports = [PDFReport(),ExcelReport()]
for report in reports:
    report.export()