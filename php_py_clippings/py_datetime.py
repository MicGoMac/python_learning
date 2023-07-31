# learn fr https://www.w3schools.com/python/python_datetime.asp

import datetime

#The datetime() class requires three parameters to create a date: year, month, day.
#also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional,

x = datetime.datetime(2020, 5, 17)
print(x)

x = datetime.datetime(2020, 5, 17, 18, 19, 20, 8)
#this not working:
print(x.timezone)

#day of month
print(x.strftime("%d"))

x = datetime.datetime.now()
print(x)
print(x.year)

datetime_code={ "short_weekday":%a, "weekday":%A,"weekday_num":%w, "0day_num":%d,"day_num":%-d,  
 "short_month":%b,"0month_num":%m,"month_num":%-m,"month":%B,  "year":%Y,"0short_year":%y,"short-yearw":%-y,
"0hour":%H,"hour":%-H,"012hour":%I,"12hour":%-I,"ampm":%p,
"0min":%M,"min":%-M,"0sec":%S, "sec":%-S, "microsec":%f,
"utc":%z,"timezone":%Z,"0dayofyear":%j,"dayofyear":%-j,
"week_num":%U,"0week_num":%W,  "locale_datetime":%c,"locale_date":%x,"locale_time":%X, "%":%%, 
}

print(x.strftime("%A"))



