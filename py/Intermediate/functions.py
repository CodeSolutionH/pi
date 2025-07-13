# Functions in Python
# -------------------
# A function is a block of code that runs when called. You can pass data (parameters) into a function, and it can return data as a result.

# Defining a function:
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# Function with a return value:
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5

# Default parameter values:
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # Output: 9
print(power(3, 3))   # Output: 27
