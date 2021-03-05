# A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

from queue import PriorityQueue

# return total num of digits in an array of stringified numbers
def digitsRemaining(nums):
  ret = 0
  for i in nums:
    ret = ret + len(i)
  return ret

def solve():
  f = open("keylog.txt", "r")
  lines = f.readlines()
  nums = list(map(lambda x: x.rstrip(), lines))

  # use a PQ so we can consider the solutions that are closest to being done first
  pq = PriorityQueue()
  pq.put((digitsRemaining(nums), ['', nums]))
  while (True):
    q = pq.get()[1]
    remainders = q[1]
    candidate = q[0]
    for i in range(0,10):
      startWithI = list(filter(lambda x: x[0] == str(i), remainders))
      if len(startWithI) > 0:
        others = list(filter(lambda x: x[0] != str(i), remainders))
        newRemainders = others + list(map(lambda x: x[1:], startWithI))
        newRemainders = list(filter(lambda x: x != '', newRemainders))
        newCandidate = candidate + str(i)
        if len(newRemainders) == 0:
          return newCandidate
        pq.put((digitsRemaining(newRemainders), [newCandidate, newRemainders]))

print(solve())