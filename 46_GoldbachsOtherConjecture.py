# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math  

# store found primes here to make things quicker
primes = []

# whether a number can be written as the sum of a prime and twice a square
# basically we iterate through all the primes we've seen so far and check
# if the remainder is 2x a perfect square. if it is, return true, if none
# are the number doesn't meet the condition
def meetsCondition(n):
  for p in primes:
    remainder = n - p
    if (remainder % 2 == 0):
      root = math.sqrt(remainder / 2)
      if ((int(root) * int(root)) == (remainder / 2)):
        return True
  return False

def isPrime(n):
  i = int(math.sqrt(n))
  while(i > 1):
    if (n%i == 0):
      return False
    i = i - 1
  primes.append(n)
  return True

def isOdd(n):
  return n % 2 == 1

def solve():
  i = 1
  while(True):
    if (not(isPrime(i)) and isOdd(i)):
      if (not(meetsCondition(i))):
        return i
    i = i + 1
  return 0

print(solve())