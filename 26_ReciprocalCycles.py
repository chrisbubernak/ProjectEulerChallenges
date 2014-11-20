#A unit fraction contains 1 in the numerator. The decimal representation
#of the unit fractions with denominators 2 to 10 are given:

#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
#It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring
#cycle in its decimal fraction part.

def getLength(n):
    i = 0;
    mod = 10;
    while(mod != 1):
        mod = ((mod * 10) % n);
        i = i + 1;
    return i;


def onlyDivisibleBy2And5(n):
    while(n%5 == 0):
        n = n/5;
    while(n%2 == 0):
        n = n/2;
    if n == 1:
        return True;
    return False;

def coprimeToTen(n):
    if n%5 == 0 or n%2 == 0:
        return False;
    return True;

def patternLength(n):
    if onlyDivisibleBy2And5(n):
        return 0;
    elif not(coprimeToTen(n)):
        return 1;
    else:
        return getLength(n);
    
def solve(n):
    l = [];
    for i in range(2, n+1):
        l.append(patternLength(i));
    return (l.index(max(l)) + 2);

print solve(1000);
