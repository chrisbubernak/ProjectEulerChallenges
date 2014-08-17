#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10,001st prime number?

import math;

def isPrime(n):
        for i in range(2, int(math.floor(n ** (.5))+1)):
                if (n%i == 0):
                        return False;
        return True;


n = 10001;
i = 2;
count = 0;
while (count < n):
        if isPrime(i):
                count = count +1;
        i = i+1;
print i-1;

