# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

cubes = dict()

def solve(n):
  i = 0
  while (True):
    cube = i ** 3
    cubeKey = str(cube)
    cubeKey = ''.join(sorted(cubeKey))
    if not(cubeKey in cubes):
      cubes[cubeKey] = list()
    cubes[cubeKey].append(cube)
    if len(cubes[cubeKey]) == n:
      return cubes[cubeKey][0]
    i = i + 1

print(solve(5))
