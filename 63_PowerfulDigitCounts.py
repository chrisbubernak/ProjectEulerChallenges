# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

def solve(n):
  finds = 0
  for i in range(1, n):
    for j in range(1, n):
      power = i ** j
      if len(str(power)) == j:
        finds = finds + 1
  return finds

# Check everything under 200 ^ 200
print(solve(200))