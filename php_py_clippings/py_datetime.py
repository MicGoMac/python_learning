# learn fr https://www.w3schools.com/python/python_datetime.asp

import datetime

#The datetime() class requires three parameters to create a date: year, month, day.
#also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional,

x = datetime.datetime(2020, 5, 17)
print(x)

x = datetime.datetime(2020, 5, 17, 18, 19, 20, 8)
#this not working:
print(x.timezone)

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))



