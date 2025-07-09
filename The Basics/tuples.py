# Tuples in Python
# ----------------
# A tuple is an ordered, immutable collection of items. Once created, the items in a tuple cannot be changed.

# How to create a tuple:
my_tuple = (1, 2, 3)
empty_tuple = ()
single_item_tuple = (5,)  # Note the comma!

# Accessing tuple items:
print(my_tuple[0])  # Output: 1

# Tuples can contain different data types:
mixed_tuple = (1, "hello", 3.14)

# Tuples are immutable:
# my_tuple[0] = 10  # This will raise a TypeError

# Tuples can be unpacked:
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3

# Tuples are often used to return multiple values from a function:
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([1, 2, 3])
print(result)  # Output: (1, 3)
