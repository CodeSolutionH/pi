# JSON in Python
# --------------
# JSON (JavaScript Object Notation) is a common data format for exchanging data.
# Python has a built-in module called 'json' to work with JSON data.

import json

# Convert Python object to JSON string:
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print(json_str)

# Convert JSON string to Python object:
parsed = json.loads(json_str)
print(parsed)

# Read/write JSON from/to a file:
# with open('data.json', 'w') as f:
#     json.dump(data, f)
# with open('data.json', 'r') as f:
#     loaded = json.load(f)
