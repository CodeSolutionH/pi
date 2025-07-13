# Inheritance in Python
# ---------------------
# Inheritance allows a class to inherit attributes and methods from another class.

# Base class (parent):
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal sound")

# Derived class (child):
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.speak()  # Output: Buddy says woof!
