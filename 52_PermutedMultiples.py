# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

# checks permutations 2x - Nx to see if they contain the same digits

def meetsCondition(num, n):
  digits = list(str(2*num))
  digits.sort()
  for i in range(3, n + 1):
    prod = i * num
    prodDigits = list(str(i * num))
    prodDigits.sort()
    if not(digits == prodDigits):
      return False
  return True

def solve(n):
  i = 1
  while(True):
    if meetsCondition(i, n):
      return i
    i = i + 1
  
print(solve(6))
