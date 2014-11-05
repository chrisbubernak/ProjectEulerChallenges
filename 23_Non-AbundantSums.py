#A perfect number is a number for which the sum of its proper divisors is exactly
#equal to the number. For example, the sum of the proper divisors of 28 would be 1
#+ 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n
#and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
#that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
#it can be shown that all integers greater than 28123 can be written as the sum of two
#abundant numbers. However, this upper limit cannot be reduced any further by analysis
#even though it is known that the greatest number that cannot be expressed as the sum
#of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two
#abundant numbers.

import math;

maxNum = 28123;

def properDivisors(n):
    d = [1];
    for i in range(2, int(math.floor(math.sqrt(n))) + 1):
        if i * i == n:
            d.append(i);
        elif n % i == 0 and n != i:
            d.append(i);
            d.append(n/i);
    return d;

def isAbundant(n):
    if sum(properDivisors(n)) > n:
        return True;
    return False;

# gets all abundant numbers less than maxNum
def getAbundantNumbers():
    a = [];
    for i in range(1, maxNum):
        if isAbundant(i):
            a.append(i);
    return a;

def solve():
    ret = 0;
    abundant = getAbundantNumbers();
    sums = [0] * maxNum;
    for i in range(0, len(abundant)):
        for j in range(0, len(abundant)):
            if ((abundant[i] + abundant[j]) < maxNum):
                sums[abundant[i] + abundant[j]] = 1; #just flip a bit
            else:
                break;
        if abundant[i] * 2 > maxNum:
            break;
    for i in range(0, maxNum):
        if sums[i] == 0:
            ret = ret + i;
    return ret;

print solve();
