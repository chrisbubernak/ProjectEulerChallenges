# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 x 1 = 192
# 192 x 2 = 384
# 192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital,
# 192384576. We will call 192384576 the concatenated product of
# 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by
# 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is
# the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can
# be formed as the concatenated product of an integer with (
# 1,2, ... , n) where n > 1?

def isPandigital(n):
    s = str(n);
    numbers = [0] * 9;
    if(len(s) != 9):
        return False;
    for i in range(0, len(s)):
        num = int(s[i]);
        if numbers[num - 1] == 1:
            return False;
        else:
            numbers[num - 1] = 1;
    return True;

def calculate(x, n):
    ret = '';
    for i in range(1, n + 1):
        ret = ret + str(x * i);
    return int(ret);

def solve():
    best = 0;
    # we can use 10,000 as an upper bound because if we use a 5 digit
    # integer we will get a 10 digit (at least) result which will be
    # too long to be pandigital
    for i in range(1, 10000):
        for j in range(2, 10):
            candidate = calculate(i, j);
            if isPandigital(candidate) and candidate > best:
                best = candidate;
    return best;


print solve();
