# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

import math
import itertools

def isPrime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if (n % i == 0):
      return False
  return True

def solve():
  # the key is the 4 digits sorted and the entries are permutations of those digits
  results = dict()

  # iterate over all 4 digit numbers
  for i in range(1000, 10000):
      chars = list(str(i))
      chars.sort()
      key = ''.join(chars)

      if isPrime(i):
        if not(key in results):
          results[key] = []
        results[key].append(i)

  # now that we have all permutations that share digits see if any combinations of 3
  # meet the criteria of being arithmetic sequences
  for key in results:
    for perm in itertools.combinations(results[key], 3):
        list(perm).sort()
        if ((perm[0] - perm[1]) == (perm[1] - perm[2])):
          result = str(perm[0]) + str(perm[1]) + str(perm[2])
          # skip answer from the prompt
          if (not(result == '148748178147')):
            return result

print(solve())
