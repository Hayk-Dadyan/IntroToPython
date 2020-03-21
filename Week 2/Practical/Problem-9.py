#Problem 9
import datetime
import time
import calendar
datetime1 = datetime.datetime.today()
tdelta = datetime.timedelta(days = 5)
print("Current date and time:",datetime1)
print("Year:" ,datetime1.year)
print("Month:" ,datetime1.month)
print("Day of the week:" ,datetime1.isoweekday())
print("5 days subtracted:" ,datetime1 - tdelta)
print("5 days added:" ,datetime1 +tdelta)