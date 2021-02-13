# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten 
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, 
# is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import math

def isPrime(n):
  for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
      return False
  return True

def belongsToFamilyOfN(num, primes, n):
  # create a set of all the "families" a number
  # could belong to
  families = set()
  for i in range(0, 10):
    families.add(num.replace(str(i), '*'))
  
  for f in list(families):
    family = set()
    # try creating all 10 numbers that could be 
    # in this family and keep them if they are 
    # known primes
    for i in range(0, 10):
      candidate = int(f.replace('*', str(i)))
      if candidate in primes:
        family.add(candidate)
      if len(family) == n:
        return True
  return False

def solve(n):
  digits = 1
  while(True):
    low = int(math.pow(10, digits)) 
    hi = int(math.pow(10, digits+1))
    primes = set()
    for i in range(low, hi):
      if isPrime(i):
        primes.add(i)
    primeList = list(primes)
    primeList.sort()
    for i in range(0, len(primeList)):
      # checks if a prime belongs to a family of size n
      if(belongsToFamilyOfN(str(primeList[i]), primes, n)):
        # if so return it b/c it will be the smallest in that family
        return primeList[i]
    # move to considering numbers of length + 1
    digits = digits + 1

print(solve(8))
