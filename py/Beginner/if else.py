# If-Else Statements in Python
# ---------------------------
# if, elif, and else are used for conditional execution.

x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# You can use if statements without else or elif:
if x > 5:
    print("x is greater than 5")

# Short-hand if statement:
print("x is positive") if x > 0 else print("x is not positive")
