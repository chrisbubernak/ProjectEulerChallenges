#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

import math;

def isPalindrome(x):
  for i in range(0, len(x)/2):
    if x[i] != x[len(x)-i-1]:
      return False;
  return True

def solve(n):
  palindromes = [];
  low = int(math.pow(10,n-1));
  hi = int(math.pow(10,n));
  for i in range(low, hi):
    for j in range(low, hi):
      if isPalindrome(str(i*j)):
        palindromes.append(i*j);
  return max(palindromes)

print solve(3);

