#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder. What is the smallest positive
#number that is evenly divisible by all of the numbers from 1 to 20?

import math;

def getFactors(x):
    factors = {};
    cur = x;
    n = 2;
    while cur > 1:
        if cur%n == 0:
            cur = cur/n;
            if n in factors.keys():
                factors[n] = factors[n] + 1;
            else:
                factors[n] = 1;
            n = 2;
        else:
            n = n + 1;
    return factors;

def updateFactors(allFactors, newFactors):
    for n in newFactors:
        if n in allFactors.keys():
            allFactors[n] = max(allFactors[n], newFactors[n]);
        else:
            allFactors[n] = newFactors[n];
    return allFactors;

def solve(n):
    ret = 1;
    factorDict = {};
    for i in range(1, n+1):
        factors = getFactors(i);
        updateFactors(factorDict, factors);
    for key in factorDict:
        ret = ret * math.pow(key, factorDict[key]);
    return int(ret);

print solve(20);
