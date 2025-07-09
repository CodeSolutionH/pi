# Arrays in Python
# ----------------
# Python does not have a built-in array type like some other languages, but you can use the 'array' module for basic arrays, or use lists for most purposes.

# Using lists as arrays:
numbers = [1, 2, 3, 4]
print(numbers)

# Using the array module:
import array
arr = array.array('i', [1, 2, 3, 4])  # 'i' means integer
print(arr)

# Arrays from the array module are more efficient for large numeric data, but less flexible than lists.

# Difference between lists and arrays:
# - Lists can hold items of different types; arrays hold only one type.
# - Lists are more commonly used in Python.
