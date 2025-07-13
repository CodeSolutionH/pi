# Match Statements in Python
# -------------------------
# The match statement (introduced in Python 3.10) is used for pattern matching, similar to switch/case in other languages.

# Example usage:
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"

print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found

# Patterns can match values, types, and structures:
def process(item):
    match item:
        case int():
            print("It's an integer!")
        case str():
            print("It's a string!")
        case [x, y]:
            print(f"A list with two items: {x}, {y}")
        case _:
            print("Something else!")

process(42)
process("hello")
process([1, 2])
