# Strings in Python
# -----------------
# A string is a sequence of characters, used to store text data.

# How to create a string:
greeting = "Hello, world!"
name = 'Alice'

# Multiline strings:
multiline = """This is
a multiline
string."""

# Accessing characters:
print(greeting[0])  # Output: H

# String concatenation:
full_greeting = greeting + " My name is " + name
print(full_greeting)

# String formatting:
formatted = f"Hello, {name}!"
print(formatted)

# Common string methods:
print(greeting.lower())  # Output: hello, world!
print(greeting.upper())  # Output: HELLO, WORLD!
print(greeting.replace("world", "Python"))  # Output: Hello, Python!

# Strings are immutable:
# greeting[0] = 'h'  # This will raise a TypeError
