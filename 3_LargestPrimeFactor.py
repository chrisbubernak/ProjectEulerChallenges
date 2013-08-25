#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

import math;

def isPrime(n):
        for i in range(2, int(math.floor(n ** (.5))+1)):
                if (n%i == 0):
                        return False;
        return True;


def solve(n):
        for i in reversed(range (1, int(math.floor(n ** (.5))+1))):
                if (n%i == 0 and isPrime(i)):
                        return i;

print solve(600851475143);
