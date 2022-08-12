import datetime
import pytz

today = datetime.date.today()

print(today)





print()

birthday = datetime.date(2002 , 2 ,19)
print(birthday)






print()

days_since_birth = (today - birthday).days

print(days_since_birth)







print()

tdelta = datetime.timedelta(days = 4)
print(today + tdelta )
print()

print(today.month)







print()

print(today.weekday())

print()

print(today.day)






print()

print(datetime.time(7,10,20,15))

#datetime.date (Y.M.D)
#datetime.Time(h,m,s,ms)
#datetime.datetime(Y,M,D,h,m,s,ms)

#add 10 hours to current day 
hour_delta = datetime.timedelta(hours = 10)

print(datetime.datetime.now() + hour_delta)

print()

datetime_today = (datetime.datetime.now(tz=pytz.UTC))


datetime_pacific =  (datetime_today.astimezone(pytz.timezone('US/Pacific')))

print(datetime_pacific)

for tz in pytz.all_timezones:
  print(tz)


#satrting formatting with dates
#2019-02-09 = augusgt 12 2022
#f= formatiing
print(datetime_pacific.strftime('%B %d ,%Y'))

# from august to like 2022 - 12 -8
#strptime  p = parsing

#datetime_thing = datetime.datetime.strptime('August 12, 2022',  '%B %d , %Y')
#print(repr(datetime_thing))