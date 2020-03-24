#Problem 5
import datetime
import time
import calendar
bday = datetime.date(2000, 9, 12)
today = datetime.date.today()
datetime_today = datetime.datetime.today()
next_bday = datetime.date(2020, 9, 12)
tdelta1 = datetime.timedelta(days = 1)
x = datetime_today - tdelta1
tdelta2 = datetime.timedelta(days = 2)
tdelta3 = datetime.timedelta(days = 3)
print("Date of birth:", bday)
print("Year of birth:", bday.year)
print("Month of birth:", bday.month)
print("Day of birth:", bday.day)
print("Day of week:", bday.isoweekday())
print("Until next birthday:", next_bday - today)
print("--------------------------------------")
print(calendar.month(2017, 5))
print("--------------------------------------")
print("Yesterday at this time:", x)
print("Yesterday + 2 days:", x + tdelta2)
print("Yesterday - 3 days:", x - tdelta3)