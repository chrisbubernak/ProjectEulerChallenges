# The number 3797 has an interesting property. Being prime itself, it
# is possible to continuously remove digits from left to right, and
# remain prime at each stage: 3797, 797, 97, and 7. Similarly we can
# work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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

def isPrime(n):
    # check if prime
    for i in range(n - 1, 1, -1):
        if n%i == 0:
            return 0;
    return 1;

def solve(n):
    ret = 0;
    primes = findPrimes(1000000); # find all primes below 1000000
    found = 0;
    cur = 10; # start at 10 b/c 2,3,5,7 don't count
    # keep looking till we find all 11!
    while (found < n):
        # maybe we will have to go above the 1000000
        # primes we initial solved for...in that case just
        # start appending
        if (cur >= len(primes)):
            primes.append(isPrime(cur));

        # only start checking truncations if the original number is prime3
        if primes[cur] == 1:
            strCur = str(cur);
            for i in range(0, len(strCur)):
                subStrL = strCur[i:];
                subStrR = strCur[:len(strCur) - i];
                if primes[int(subStrR)] == 0 or primes[int(subStrL)] == 0:
                    break;
                elif i == len(strCur) - 1:
                    ret = ret + cur;
                    found = found + 1;
        cur = cur + 1;
    return ret;

print solve(11);

