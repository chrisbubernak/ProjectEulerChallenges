# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large:
# one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

def digitSum(n):
  total = 0
  numStr = str(n)
  for digit in numStr:
    total = total + int(digit)
  return total

def solve(n):
  best = 0
  for i in range(1, n):
    for j in range(1, n):
      candidate = digitSum(i ** j)
      if (candidate > best):
        best = candidate
  return best

print(solve(100))
