import random

import time


def getrandomdate(startdate,enddate):
    print(""Printing random date between", starDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(starDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat,time.localtime(randomtime)))
    return randomdate


print("Random Date = ", getRandomDate("1/1/2020", "12/12/2024"))


