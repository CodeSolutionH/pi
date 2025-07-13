# While Loops in Python
# ---------------------
# A while loop repeats as long as a condition is True.

count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# Infinite loop (be careful!):
# while True:
#     print("This will run forever")

# Using break to exit a loop:
count = 0
while True:
    print(count)
    count += 1
    if count == 3:
        break
