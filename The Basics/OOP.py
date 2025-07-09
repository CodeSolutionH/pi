# Object-Oriented Programming (OOP) in Python
# -------------------------------------------
# OOP is a programming paradigm based on the concept of objects, which contain data and methods.

# Key principles:
# - Encapsulation: Bundling data and methods together
# - Inheritance: Deriving new classes from existing ones
# - Polymorphism: Using a unified interface for different data types
# - Abstraction: Hiding complex details and showing only essentials

# Example of a class and object:
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says woof!
