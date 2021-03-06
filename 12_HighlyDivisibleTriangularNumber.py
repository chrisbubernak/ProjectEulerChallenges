#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1,3
# 6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.

#What is the value of the first triangle number to have over five hundred divisors?

import math;

def getDivisors(n):
  d = 0;
  sqrt = int(math.floor(math.sqrt(n)));
  if (sqrt == 0 or(n%sqrt) == 0):
    d+=1;
  for i in range(1, sqrt):
    if ((n%i) == 0):
      d+=2;
  return d;
  
def solve(threshold):
  i = 1;
  n = 0;
  while (getDivisors(n) < threshold):
    n+=i;
    i+=1;
  return n



cache = []
compares = 0
print solve(500)

