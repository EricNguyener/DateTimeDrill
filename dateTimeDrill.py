from datetime import datetime
from pytz import timezone

nowUTC = datetime.now(timezone('UTC'))

##Formatting the time
fmt = "%I:%M %p %a, %d %b %Y"

##Timezones 
timezonelist = {
'Portland ': (nowUTC.astimezone(timezone('US/Pacific'))),
'New York ': (nowUTC.astimezone(timezone('US/Eastern'))),
'London   ': (nowUTC.astimezone(timezone('Europe/London')))
}

def officeTime(timezonelist):
    for key, value in timezonelist.items():
        hr = value.strftime('%H')
        branch = key
        locationTime = value.strftime(fmt)
        if int(hr) >= 9 and int(hr) < 21:
            print "Open\t" + branch + locationTime
        else:
            print "Closed\t" + branch + locationTime
            
officeTime(timezonelist)









