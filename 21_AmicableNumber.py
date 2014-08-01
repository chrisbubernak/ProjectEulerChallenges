#Problem 21
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

import math

#calculates d for a given number
def d(n):
    sum = 0
    for i in range(1, n):
        if n%i == 0:
            sum = sum + i 
    return sum

def solve(n):
    sum = 0
    solved = {}
    for i in range(1, n):
        s = d(i)
        solved[i] = s
        if s in solved.keys():
            if i == solved[s] and solved[i] != i:
                sum = (sum + i + s)
    return sum

print solve(10000)
