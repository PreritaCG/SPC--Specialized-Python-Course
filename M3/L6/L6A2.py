from datetime import date,time,datetime
#calling the today
#fuctions of date class
today=date.today()
now=datetime.now()
print ("todays date is",now)

#printing date's componets
print("\nDate componets",today.year,
today.month,today.day)


import random #importing module 
import time

def getRandomDate(startDate, endDate):#defining function
    print("printing random date between",startDate," and", endDate)
    randomGenertor=random.random()
    dateFormat='%m/%d/%y'
    startTime=time.mktime(time.strptime(startDate,dateFormat))
    endTime= time.mktime(time.strptime(endDate,dateFormat))
    randomTime=startTime+randomGenertor*(endTime-startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
#display result
print("Random Date=",getRandomDate("1/1/2016","12/12/2018"))