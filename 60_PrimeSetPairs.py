# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any
# order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum
# of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import itertools
import math

primesCache = set()

def isPrime(n):
  if n in primesCache:
    return True
  if n == 1:
    return False
  for i in range(2, 1+int(math.sqrt(n))):
    if (n % i == 0):
      return False

  primesCache.add(n)
  return True

def getPrimesBelow(n):
  ret = []
  for i in range(0, n):
    if (isPrime(i)):
      ret.append(i)
  return ret

def meetsCondition(primes):
  for combo in itertools.combinations(primes, 2):
    num1 = str(list(combo)[0])
    num2 = str(list(combo)[1])
    if not(isPrime(int(num1 + num2)) and isPrime(int(num2 + num1))):
      return False
  return True

  

def solve():
  # precompute primes < 10,000 to start - this number is fairly arbitrary
  # but is a good guess for an upper bound on the answer
  primes = getPrimesBelow(10_000)

  for i in range(0, len(primes)):
    for j in range(i + 1, len(primes)):
        if not(meetsCondition([primes[i], primes[j]])):
            continue
        for k in range(j + 1, len(primes)):
            if not(meetsCondition([primes[i], primes[j], primes[k]])):
                continue
            for l in range(k + 1, len(primes)):
                if not(meetsCondition([primes[i], primes[j], primes[k], primes[l]])):
                    continue
                for m in range(l + 1, len(primes)):
                    if meetsCondition([primes[i], primes[j], primes[k], primes[l], primes[m]]):
                        print([primes[i], primes[j], primes[k], primes[l], primes[m]])
                        return sum([primes[i], primes[j], primes[k], primes[l], primes[m]])

print(solve())
