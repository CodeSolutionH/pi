# Variables in Python
# -------------------
# A variable is a container for storing data values. In Python, you do not need to declare the type of variable explicitly; the type is inferred from the value assigned.

# How to create a variable:
x = 5           # integer
name = "Alice"  # string
pi = 3.14       # float
is_valid = True # boolean

# You can change the value and type of a variable at any time:
x = "Hello"     # Now x is a string

# Variable names can contain letters, numbers, and underscores, but cannot start with a number.
# Examples of valid variable names:
user_age = 25
_user = "Bob"
user2 = "Charlie"

# Examples of invalid variable names (will cause errors):
# 2user = "Dave"
# user-age = 30

# Types of variables in Python:
# - int: Integer numbers (e.g., 1, 100, -5)
# - float: Decimal numbers (e.g., 3.14, -0.001)
# - str: Text (e.g., "hello", 'world')
# - bool: Boolean values (True or False)
# - list: Ordered collection (e.g., [1, 2, 3])
# - tuple: Immutable ordered collection (e.g., (1, 2, 3))
# - dict: Key-value pairs (e.g., {"name": "Alice", "age": 25})
# - set: Unordered collection of unique items (e.g., {1, 2, 3})

# Example:
number = 10          # int
greeting = "Hi!"     # str
price = 19.99        # float
is_active = False    # bool
items = [1, 2, 3]    # list
person = {"name": "Eve", "age": 22}  # dict
unique_numbers = {1, 2, 3}  # set

print(number, greeting, price, is_active, items, person, unique_numbers)
