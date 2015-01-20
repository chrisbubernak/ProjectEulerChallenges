# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
import math;

factorial = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880
    }

def sumEqualsNumber(n):
    s = 0;
    strN = str(n);
    for i in strN:
        s = s + factorial[int(i)];
        if (s > n): # break early
            return False;
    if s == n:
        return True;
    return False;

def solve():
 ret = 0;
 # get an upper bound...not sure how to make it
 # tigher than this but this is definitely an
 # over conservative bound
 cur = 1;
 while (factorial[9] * cur > math.pow(10, cur)):
     cur = cur + 1;
 upperBound = int(math.pow(10, cur-1));

 for i in range(10, upperBound):
     if sumEqualsNumber(i):
         ret = ret + i;
 return ret;

print solve();
