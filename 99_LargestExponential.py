# Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

# However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on 
# each line, determine which line number has the greatest numerical value.

# NOTE: The first two lines in the file represent the numbers in the example given above.

def compare(baseA, expA, baseB, expB):
  while not((baseA >= baseB and expA >= expB) or (baseA <= baseB and expA <= expB)):
    if (expA > expB):
      expA = expA - expB
      baseB = baseB / baseA
    else:
      expB = expB - expA
      baseA = baseA / baseB

  return baseA >= baseB

def solve():
  bestNum = 0
  bestPow = 0
  bestLine = 0
  line = 0
  f = open("base_exp.txt", "r")
  lines = f.readlines()
  for l in lines:
    line = line + 1
    nums = l.rstrip('\n').split(',')
    canNum = int(nums[0])
    canPow = int(nums[1])
    if not(compare(bestNum, bestPow, canNum, canPow)):
      bestNum = canNum
      bestPow = canPow
      bestLine = line
  return bestLine

print(solve())
