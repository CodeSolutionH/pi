# Lists in Python
# ---------------
# A list is an ordered, mutable collection of items.

# How to create a list:
fruits = ["apple", "banana", "cherry"]
empty_list = []

# Accessing list items:
print(fruits[0])  # Output: apple

# Modifying lists:
fruits.append("orange")
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Removing items:
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']

# Lists can contain different data types:
mixed = [1, "hello", 3.14]

# List slicing:
print(fruits[1:])  # Output: ['blueberry', 'orange']
