"""A vaccination calculator."""

__author__ = "730314515"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population : int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percentage: int = int(input("Target percent vaccinated: "))

target_time: int = int(round(doses_administered / doses_per_day))
today: datetime = datetime.today()
need_day: timedelta = timedelta(target_time)
future_day: datetime = today + need_day

future_str: str = future_day.strftime("%B %d, %Y")
target_per_str: str = str(target_percentage)
target_time_str: str = str(target_time)

print("We will reach " + target_per_str + " % vaccination in " + target_time_str + " days, which falls on " + future_str)