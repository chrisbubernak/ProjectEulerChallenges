# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?

# object mapping pentagons to their n value
# key: pentagon, value: n

# set of all pentagonals for quick lookup
pSet = {1}

# array of pentagonal values so we know which we've calculated
pentagonals = [1]

# generates a pentagonal number
def pentagonal(n):
  return n*(3*n-1)/2

def isPentagonal(p):
  # if p > than the biggest thing in our array we need to generate
  # some more pentagonals
  while(p > pentagonals[len(pentagonals) - 1]):
    nextN = len(pentagonals) + 1
    nextP = pentagonal(nextN)
    # for each new one add it to the set (for quick checks)
    pSet.add(nextP)
    # add the new one to the list 
    pentagonals.append(nextP)

  return p in pSet

def solve(n):
  for j in range(1, n):
    for k in range(1, n): 
      pj = pentagonal(j)
      pk = pentagonal(k)
      if (isPentagonal(pj+pk) and isPentagonal(abs(pj-pk))):
        return int(abs(pj-pk))

# for simplicity just keep choosing bigger n values until this returns an answer
print(solve(3000))
