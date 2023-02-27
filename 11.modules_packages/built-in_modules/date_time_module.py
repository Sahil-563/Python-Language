from datetime import date
print(date.today())  #date.today() is used to print the date that is currently running in your system
print(date.today().year)  #by this method we can call the year of a particular date
print(date.today().month)  #by this method we can call the month of a particular date
print(date.today().day)  #by this method we can call the month of a particular date

from datetime import datetime
print(datetime.now())  #this is used to print the current date and time running in you pc
time1 = datetime(year = 2021,month=3,day=14,hour = 2,minute=8,second=20) #user cereated date and time
print(time1)

timenow = datetime.now()
timediff = timenow - time1
print(timediff)
print(timediff.total_seconds())   #this method is used to print the difference between two times and show its seconds
