# It is possible to show that the square root of two can be expressed as an infinite continued fraction.

# sqrt(2) = 1 + 1 / ( 2 + 1 / (2 + 1 / (2 + 1 / ...)))

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5

# 1 + 1/(2 + 1/2) = 7/5 = 1.4

# 1 + 1/(2 + 1 / (2 + 1/2)) = 17/12 = 1.41666...

# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion , 1393/985, is the first example where the number of digits
# in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

# 1/(2 + (num/den)) returns a tuple of numerator and denominator
def add(n, d):
  return [d, 2*d+n]

# def getNum(n, d):
#   return d

# def getDen(n, d):
#   return 2*d+n

# see if 1 + n/d has more digits in the numerator
def check(n, d):
  return len(str(n+d)) > len(str(d))

def solve(n):
  count = 0
  num = 1
  den = 2
  for i in range(0, n):
    [num,den] = add(num, den)
    if (check(num, den)):
      count = count + 1
  return count

print(solve(1000))
