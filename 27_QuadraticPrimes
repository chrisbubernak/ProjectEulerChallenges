#Euler discovered the remarkable quadratic formula:

#n^2 + n + 41

#It turns out that the formula will produce 40 primes for
#the consecutive values n = 0 to 39. However, when n = 40,
#402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and
#certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

#The incredible formula  n^2 - 79n + 1601 was discovered,
#which produces 80 primes for the consecutive values n = 0 to 79.
#The product of the coefficients, -79 and 1601, is -126479.

#Considering quadratics of the form:

#n^2 + an + b, where |a| < 1000 and |b| < 1000

#where |n| is the modulus/absolute value of n
#e.g. |11| = 11 and |-4| = 4

#Find the product of the coefficients, a and b, for the quadratic
#expression that produces the maximum number of primes for consecutive
#values of n, starting with n = 0.

def isPrime(n, primes):
    return primes[n] == 1;

def calculate(n, a, b):
    return n*n + a*n + b;

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


def solve(x):
    ret = 0;
    # find all primes less than x*x ...we could probably use 
    # a tighter bound here but this works
    primes = findPrimes(x*x);
    maxPrimes = 0;
    for a in range(-x, x):
        for b in range(-x, x):
            count = 0;
            n = 0;
            while (isPrime(calculate(n, a, b), primes)):
                n = n + 1;
                count = count + 1;
            if (count > maxPrimes):
                ret = a * b;
                maxPrimes = count;
    return ret;

print solve(1000);
