# Type Casting in Python
# ----------------------
# Type casting is converting a value from one data type to another.

# Common casting functions:
# int(), float(), str(), bool(), list(), tuple(), set(), dict()

# Examples:
x = "123"
y = int(x)  # Convert string to int
print(y, type(y))  # Output: 123 <class 'int'>

z = 3.14
w = str(z)  # Convert float to string
print(w, type(w))  # Output: '3.14' <class 'str'>

# Casting list to set (removes duplicates):
nums = [1, 2, 2, 3]
unique_nums = set(nums)
print(unique_nums)  # Output: {1, 2, 3}
