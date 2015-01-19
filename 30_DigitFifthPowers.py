# Surprisingly there are only three numbers that can be written as the
# sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.

import math;

def canBeWrittenAsSumOfPowers(n, power):
    s = 0;
    string = str(n);
    for digit in string:
        s = s + math.pow(int(digit), power);
    if (n == s):
        return True;

def findMaxNumber(n):
    i = 1;
    while(int('9'*i) < math.pow(9,n)*i):
        i = i + 1;
    return int(math.pow(9,n)*i);

def solve(n):
    numbers = [];
    maxNum = findMaxNumber(n);
    for i in range(10, 354294):
        if (canBeWrittenAsSumOfPowers(i, n)):
            numbers.append(i);
    return sum(numbers);


print solve(5);
