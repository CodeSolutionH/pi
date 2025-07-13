# Datetime Module in Python
# ------------------------
# The datetime module allows you to work with dates and times.

import datetime

# Current date and time:
now = datetime.datetime.now()
print(now)

# Create a specific date:
d = datetime.date(2023, 1, 1)
print(d)

# Format dates:
print(now.strftime("%Y-%m-%d %H:%M:%S"))
