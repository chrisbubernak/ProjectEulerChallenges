# We shall say that an n-digit number is pandigital if it makes use of
# all the digits 1 to n exactly once. For example, 2143 is a 4-digit
# pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

import math;

# gets all pandigital permutations of n digits and returns them in descending
# order
def getPermutations(n):
    # Find the largest index k such that a[k] < a[k + 1]. If no such index
    # exists, the permutation is the last permutation.
    # Find the largest index l greater than k such that a[k] < a[l].
    # Swap the value of a[k] with that of a[l].
    # Reverse the sequence from a[k + 1] up to and including the final
    # element a[n].
    cur = '';
    for i in range(1, n + 1):
        cur = cur + str(i);
    k = len(cur) - 2;
    end = cur[::-1];
    ret = [cur];
    while (cur != end):
        if int(cur[k]) < int(cur[k + 1]):
            l = len(cur) - 1;
            while(int(cur[k]) > int(cur[l])):
                l = l - 1;
            cur = cur[:k] + cur[l] + cur[k + 1:l] + cur[k] + cur[l + 1:];
            front = cur[:k + 1];
            back = cur[k + 1:len(cur)];
            cur = front + back[::-1];
            ret.append(cur);
            k = len(cur) - 1;
        k = k - 1;
        i = i + 1;
    return ret[::-1];

def isPrime(n):
    # check if prime
    s = int(math.sqrt(n)) + 1;
    for i in range(2, s):
        if n%i == 0:
            return 0;
    return 1;

def solve():
  # if the sum of a numbers digits is divisible by 3 then the number
  # can't be prime, because of this we can rule out all 8 and 9 digit
  # pan-digitals and start our search at n = 7
  n = 7;
  for i in range(n, 0, -1):
      p = getPermutations(i);
      for j in range(0, len(p)):
          if isPrime(int(p[j])) == 1:
              return p[j];

print solve();
