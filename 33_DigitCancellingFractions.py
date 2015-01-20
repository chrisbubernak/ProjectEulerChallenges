# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
# correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

import math;

def isCurious(i, j):
    strI = str(i);
    strJ = str(j);
    if "0" in strI or "0" in strJ or j <= i:
        return False;
    for digit in strI:
        if digit in strJ:
            newI = strI.replace(digit, "", 1);
            newJ = strJ.replace(digit, "", 1);
            if (int(newI)/float(newJ)) == i/float(j):
                return True;
    return False;
        
def getDenominator(n, d):
    for i in range(min(n, d), 1, -1):
        if n%i == 0 and d% i == 0:
            n = n/i;
            d = d/i;
    return d;
    
def solve(n):
    iProd = 1;
    jProd = 1;
    upperBound = int(math.pow(10, n));
    lowerBound = int(math.pow(10, n - 1));
    for i in range(lowerBound, upperBound):
        for j in range(lowerBound, upperBound):
            if isCurious(i, j):
                iProd = iProd * i;
                jProd = jProd * j;
    return getDenominator(iProd, jProd);

print solve(2);
