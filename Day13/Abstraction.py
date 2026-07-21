        #Abstraction
    #Abstractiion hides implementation details and exposes only what's necessary
    
    #Python provides the abc modules for abstract classes
    
from abc import ABC, abstractmethod
import math

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

# Child class
class Car(Vehicle):
    def start(self):
        print("Car Started")


# Exercise 3: Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


car = Car()
car.start()

rect = Rectangle(5, 4)
circle = Circle(3)

print("Rectangle area:", rect.area())
print("Circle area:", circle.area())