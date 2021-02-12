# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import math

def isPrime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if (n % i == 0):
      return False
  return True

def solve(n):
  # ordered list of all primes from 1 - n, this is overkill as we will never need numbers
  # this big to actually create a running sum to n but it makes life simple
  primes = list()
  for i in range(1, n):
    if(isPrime(i)):
      primes.append(i)
  
  # the longest sequence length
  mostPrimes = 0
  # the number to return
  mostPrimesNum = 0

  # start a sequence from each known prime, there is probably a good place we can bail
  # before trying all starting sequences but this is simple
  for i in range(1, len(primes)):
    curTotal = 0
    j = i
    # for each starting prime we are going to consider all sequence lengths from 1 to
    # the remaining length of the list
    while (curTotal <= n) and j < len(primes):
      # the length of the sum we are considering
      seqLength = j - i + 1
      curTotal = curTotal + primes[j]
      # if the length is longer then the current best and the total is actually prime
      # replace our current winner
      if (seqLength > mostPrimes) and (isPrime(curTotal)):
        mostPrimes = seqLength
        mostPrimesNum = curTotal
      j = j + 1
  return mostPrimesNum

print(solve(1000000))
