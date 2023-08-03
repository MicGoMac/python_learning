# learn fr https://www.w3schools.com/python/python_datetime.asp
# and https://www.pauldesalvo.com/how-to-set-a-timezone-for-a-datetime-object-in-python/

import datetime
import pytz

#The datetime() class requires three parameters to create a date: year, month, day.
#also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional,

#datetime is an obj inside datetime, so the datetime.datetime
x = datetime.datetime(2020, 5, 17)
print("1>>" + str(x))

tz=pytz.timezone("Asia/Hong_kong")
x = datetime.datetime(2020, 5, 17, 18, 19, 0, 0 , tzinfo=tz)
#this not working:
print(x)

#day of month
print(x.strftime("%d"))

x = datetime.datetime.now(tz)
print(x)
print(x.year)

#delete timezone
y=x.replace(tzinfo=None)
print(y)
print("\n")

frtimestamp  = datetime.datetime.fromtimestamp(1627759944, tz=tz)
print(frtimestamp)

datetime_code={ "short_weekday":"%a", "weekday":"%A","weekday_num":"%w", "0day_num":"%d","day_num":"%-d",  
 "short_month":"%b","0month_num":"%m","month_num":"%-m","month":"%B",  "year":"%Y","0short_year":"%y","short-yearw":"%-y",
"0hour":"%H","hour":"%-H","012hour":"%I","12hour":"%-I","ampm":"%p",
"0min":"%M","min":"%-M","0sec":"%S", "sec":"%-S", "microsec":"%f",
"utc":"%z","timezone":"%Z","0dayofyear":"%j","dayofyear":"%-j",
"week_num":"%U","0week_num":"%W",  "locale_datetime":"%c","locale_date":"%x","locale_time":"%X", "%":"%%", 
}

print(x.strftime( datetime_code["timezone"]))
#return HKT

