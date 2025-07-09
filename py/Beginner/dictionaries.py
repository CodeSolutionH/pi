# Dictionaries in Python
# ----------------------
# A dictionary is a collection of key-value pairs.

# How to create a dictionary:
person = {"name": "Alice", "age": 25}
empty_dict = {}

# Accessing values:
print(person["name"])  # Output: Alice

# Adding or updating values:
person["age"] = 26
person["city"] = "New York"
print(person)

# Removing a key:
del person["city"]
print(person)

# Iterating over keys and values:
for key, value in person.items():
    print(key, value)
