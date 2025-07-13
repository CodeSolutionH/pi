# Polymorphism in Python
# ----------------------
# Polymorphism allows functions or methods to use objects of different types through a common interface.

# Example with functions:
def add(a, b):
    return a + b

print(add(1, 2))        # Works with integers
print(add("a", "b"))    # Works with strings

# Example with classes:
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()

animal_sound(Dog())
animal_sound(Cat())
