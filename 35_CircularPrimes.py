# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
# 71, 73, 79, and 97.

# How many circular primes are there below one million?

def findPrimes(n):
    # find all the prime numbers less than or equal to a given
    # integer n using Eratosthenes' method...

    primes = [1] * n;

    # by definition these are not prime
    primes[0] = 0;
    primes[1] = 0;
    
    # Initially, let p equal 2, the first prime number.
    p = 2;

    while (p < n):
        i = 2;
        cur = p*i;
        while (cur < n):
            primes[cur] = 0;
            i = i + 1;
            cur = p * i;

        nextP = p + 1;
        while (nextP < n and primes[nextP] == 0):
            nextP = nextP + 1;
        p = nextP;
    return primes;

def circularPrime(n, primes):
    nStr = str(n);
    for i in range(0, len(nStr)):
        c = nStr[-1];
        nStr = nStr[:-1];
        nStr = c + nStr;
        if primes[int(nStr)] == 0:
            return False;
    return True;

def solve(n):
    ret = 0;
    primes = findPrimes(n);
    for i in range(0, len(primes)):
        if primes[i] == 1:
            if circularPrime(i, primes):
                ret = ret + 1;
    return ret;

print solve(1000000);
