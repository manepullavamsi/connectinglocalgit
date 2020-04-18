'''Given a date in DD-MMM-YYYY format, you need to print the next date.
Input: Given date 13-JAN-1982

Output: 14-JAN-1982'''
'''year,month,day=input("year,month,day").split(" ")
day=int(day)
print(day+1,month,year)'''
import datetime
date_entry=input('enter a date')
year,month,day=map(int,date_entry.split(" "))
date=datetime.date(year,month,day)
day=1
day+=int(date.strftime("%d"))

if(day<=30):
    print(str(day)+" - "+str(date.strftime("%b"))+" - "+str(date.strftime("%Y")))
elif(day>30 and month!=12):
    month=1
    month+=int(date.strftime("%m"))
    date=datetime.date(year,month,day)
    day=1
    print(str(day)+" - "+str(date.strftime("%b"))+" - "+str(date.strftime("%Y")))
elif(day>30 and month == 12 ):
    month=1
    day=1
    year=1
    year+=int(date.strftime("%Y"))
    print(str(day)+"-"+str(month)+"-"+str(year))
    
