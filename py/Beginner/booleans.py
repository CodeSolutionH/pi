# Booleans in Python
# ------------------
# A boolean represents one of two values: True or False.

x = True
y = False

# Booleans are often the result of comparisons:
print(5 > 3)   # Output: True
print(2 == 4)  # Output: False

# Booleans in conditions:
if x:
    print("x is True")
else:
    print("x is False")

# The bool() function can convert values to boolean:
print(bool(0))      # Output: False
print(bool(123))    # Output: True
print(bool(""))     # Output: False
print(bool("abc"))  # Output: True
