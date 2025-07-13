# Regular Expressions (RegEx) in Python
# -------------------------------------
# Regular expressions are used for matching patterns in text.

import re

# Example: Check if a string contains digits
text = "Hello123"
if re.search(r"\d+", text):
    print("Contains digits!")

# Example: Find all words in a string
words = re.findall(r"\w+", text)
print(words)

# Example: Replace digits with X
new_text = re.sub(r"\d", "X", text)
print(new_text)
