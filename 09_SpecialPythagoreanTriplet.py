#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math;

def solve(n):
  max = math.floor(math.sqrt(n/2));
  for a in range(1, n):
    for b in range(1, n):
      c = math.sqrt(a*a+b*b);
      if (a+b+c == n):
        return int(a*b*c);
  return -1;

print solve(1000);
