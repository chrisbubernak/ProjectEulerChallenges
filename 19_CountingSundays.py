#You are given the following information, but you may prefer to do some
#research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century
#unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century
#(1 Jan 1901 to 31 Dec 2000)?

#given the year, returns the # of days

def isLeapYear(year):
    if (year % 4 == 0):
        if (year % 100 == 0) and (year % 400 != 0):
            return False;
        return True;
    return False;

def daysPerYear(year):
    if isLeapYear(year):
        return 366;
    return 365;

def isFirstOfMonth(i, year):
    feb = 28;
    if isLeapYear(year):
        feb = 29;
    if (i == 0 or
        i == (31) or
        i == (31 + feb) or
        i == (31 + feb + 31) or
        i == (31 + feb + 31 + 30) or
        i == (31 + feb + 31 + 30 + 31) or
        i == (31 + feb + 31 + 30 + 31 + 30) or
        i == (31 + feb + 31 + 30 + 31 + 30 + 31) or
        i == (31 + feb + 31 + 30 + 31 + 30 + 31 + 31) or
        i == (31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30) or
        i == (31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) or
        i == (31 + feb + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30)): 
        return True;
    return False;

def isSunday(totalDays):
    return totalDays% 7 == 5;

def solve():
    numOfSundays = 0;
    totalDays = 0;
    for i in range(1901, 2001):
        days = daysPerYear(i);
        for j in range(0, days):
            if (isSunday(totalDays + j) and isFirstOfMonth(j, i)):
                numOfSundays += 1;
        totalDays = totalDays + days;
    return numOfSundays;

print solve();

