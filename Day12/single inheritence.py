class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    pass

dog = Dog()
dog.speak()

    #The Dog class inherits speak() method from Animal.

   
   
    
    #3.Child class with Additional MEthods
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
dog = Dog()
dog.eat()
dog.bark()




        #Multilevel Inheritence
class A:
    def display(self):
        print("Class A")
class B(A):
    pass
class C(B):
    pass

obj = C()

obj.display()




        #Multiple Inheritence
class Camera():
    def capture(self):
        print("Taking photo")
class phone:
    def call(self):
        print("Calling")
class Smartphone(Camera,phone):
    pass
obj = Smartphone()
obj.capture()
obj.call()