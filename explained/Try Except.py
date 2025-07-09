# Try-Except in Python
# --------------------
# Use try-except blocks to handle errors (exceptions) gracefully.

# Example:
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("That was not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This always runs.")

# The 'finally' block is optional and runs no matter what.
