# Scope in Python
# ---------------
# Scope refers to the region where a variable is recognized.

# Global variable:
x = 10

def foo():
    # Local variable:
    y = 5
    print(x)  # Can access global x
    print(y)  # Can access local y

foo()
# print(y)  # Error: y is not defined outside foo()

# To modify a global variable inside a function, use 'global':
def bar():
    global x
    x = 20

bar()
print(x)  # Output: 20
