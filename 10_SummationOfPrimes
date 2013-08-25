#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

import math;

def isPrime(n):
        for i in range(2, int(math.floor(n ** (.5))+1)):
                if (n%i == 0):
                        return False;
        return True;


n = 2000000;
total = 0;
for i in range(2, n):
        if isPrime(i):
                total = total + i;
print total;
