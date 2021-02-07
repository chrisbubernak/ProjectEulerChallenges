# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import math  

def isPrime(n):
  return len(factors(n)) == 0

def factors(n):
  factors = set()
  root = int(math.sqrt(n))
  for i in range(2, root + 1):
    if (n % i == 0):
        factors.add(i)
        factors.add(int(n/i))
  return list(factors)

# returns true if num has n distinct primes
def hasNDistinctPrimeFactors(num, n):
  primeCount = 0
  f = factors(num)
  for factor in f:
    if isPrime(factor):
      primeCount = primeCount + 1
    if primeCount == n:
      return True
  return False

def solve(n):
  # the number of consecutive matches we have
  consecutive = 0

  i = 0
  # go until we have the correct number of matches
  while(consecutive != n):
    if (hasNDistinctPrimeFactors(i, n)):
      consecutive = consecutive + 1
    else:
      consecutive = 0
    i = i + 1
  # return the first number of this sequence
  return i - n
    
print(solve(4))