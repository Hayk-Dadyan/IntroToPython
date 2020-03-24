#Problem 1
import datetime
import time
num_y = int(input())
num_d = int(input())
datetime1 = datetime.datetime.today()
tdelta1 = datetime.timedelta (days = 365)
tdelta2 = datetime.timedelta (days = 1)
print("Current date:" ,datetime1)
print("Given years:" ,num_y)
print("Given days:" ,num_d)
print("Final date:" ,datetime1 - (num_y * tdelta1) - (num_d * tdelta2))