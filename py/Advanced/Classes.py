# Classes in Python
# -----------------
# A class is a blueprint for creating objects (instances).

# Defining a class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object:
p1 = Person("Alice", 30)
p1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
