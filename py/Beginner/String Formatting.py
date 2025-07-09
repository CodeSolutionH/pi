# String Formatting in Python
# --------------------------
# There are several ways to format strings in Python.

# 1. f-strings (Python 3.6+):
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# 2. str.format() method:
print("My name is {} and I am {} years old.".format(name, age))

# 3. Percent (%) formatting:
print("My name is %s and I am %d years old." % (name, age))

# f-strings are the most modern and recommended way.
