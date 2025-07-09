# Lambda Functions in Python
# -------------------------
# A lambda function is a small anonymous function defined with the lambda keyword.

# Syntax:
# lambda arguments: expression

# Example:
square = lambda x: x * x
print(square(5))  # Output: 25

# Lambda functions can have multiple arguments:
add = lambda a, b: a + b
print(add(2, 3))  # Output: 5

# Common use: passing a simple function as an argument
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16]
