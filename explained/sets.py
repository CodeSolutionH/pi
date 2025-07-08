# Sets in Python
# --------------
# A set is an unordered collection of unique items.

# How to create a set:
my_set = {1, 2, 3}
empty_set = set()

# Adding and removing items:
my_set.add(4)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# Sets do not allow duplicate values:
duplicate_set = {1, 2, 2, 3}
print(duplicate_set)  # Output: {1, 2, 3}

# Set operations:
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}

# Sets are unordered and cannot be indexed:
# my_set[0]  # This will raise a TypeError
