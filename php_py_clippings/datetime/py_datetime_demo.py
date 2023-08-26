# learn fr https://www.w3schools.com/python/python_datetime.asp
# and https://www.pauldesalvo.com/how-to-set-a-timezone-for-a-datetime-object-in-python/

import datetime
import pytz

#The datetime() class basic creation: year, month, day.
#optional + (hour, minute, second, microsecond, tzone)

#datetime is an obj inside datetime, so the datetime.datetime
x = datetime.datetime(2020, 5, 17)
print("1>>simple yyyy-mm-dd" + str(x))

#this be used on every script
tz=pytz.timezone("Asia/Hong_kong")

x = datetime.datetime(2020, 5, 17, 18, 19, 0, 0 , tzinfo=tz)
print ("the full data datetime with tz")
print(x)

#day of month
print( "day of month:" + x.strftime("%d"))

x = datetime.datetime.now(tz)
print("Now with tz:")
print(x)
print(x.year)

print( "take away tz")
#delete timezone
y=x.replace(tzinfo=None)
print(y)
print("\n")

frtimestamp  = datetime.datetime.fromtimestamp(1627759944, tz=tz)
print( "timestamp to date w tz ")
print(frtimestamp)

totimestamp = int( round( datetime.datetime.timestamp(frtimestamp) ))
print(totimestamp)

#add one day's seconds to timestamp, to advance one day
oneday = totimestamp + (60*60*24)
oneday_frtimestamp  = datetime.datetime.fromtimestamp( oneday)
print(oneday_frtimestamp)

datetime_code={ "short_weekday":"%a", "weekday":"%A","weekday_num":"%w", "0day_num":"%d","day_num":"%-d",  
 "short_month":"%b","0month_num":"%m","month_num":"%-m","month":"%B",  "year":"%Y","0short_year":"%y","short-yearw":"%-y",
"0hour":"%H","hour":"%-H","012hour":"%I","12hour":"%-I","ampm":"%p",
"0min":"%M","min":"%-M","0sec":"%S", "sec":"%-S", "microsec":"%f",
"utc":"%z","timezone":"%Z","0dayofyear":"%j","dayofyear":"%-j",
"week_num":"%U","0week_num":"%W",  "locale_datetime":"%c","locale_date":"%x","locale_time":"%X", "%":"%%", 
}

print(x.strftime( datetime_code["timezone"]))
#return HKT

