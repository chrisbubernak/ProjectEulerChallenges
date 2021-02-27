# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting
# is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
# If this process is continued, what is the side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?

import math

def isPrime(n):
  for i in range(2, 1+int(math.sqrt(n))):
    if (n % i == 0):
      return False
  return True

# returns all of the diaganol numbers for a side length
def getDiaganols(n):
  square = n * n
  return [square, square - (n-1), square - 2*(n-1), square - 3*(n-1)]  

def solve(n):
  i = 1
  primes = 0
  nonPrimes = 1
  # add the or i == 1 to prevent bailing immediately when 0 < n
  while((primes / (primes + nonPrimes)) > n or (i == 1)):
    # side lengths increase by 2 each time
    i = i + 2
    diagonals = getDiaganols(i)
    for d in diagonals:
      if isPrime(d):
        primes = primes + 1
      else:
        nonPrimes = nonPrimes + 1
  return i

print(solve(.1))
