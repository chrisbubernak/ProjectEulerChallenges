# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include
# leading zeros.)

import math;

def isPalindrome(s):
    for i in range(0, len(s)):
        j = len(s) - i - 1;
        if (j == i):
            return True;
        if s[j] != s[i]:
            return False;
    return True;

def toBinary(n):
    # figure out what power of 2 to start at...
    cur = 1;
    i = 1;
    while (cur < n):
        i = i + 1;
        cur = cur *2;

    # then just keep subtracting powers of 2
    # starting from big to small
    ret = "";
    remainder = n;
    for j in range(0, i):
        temp = math.pow(2, i - j - 1);
        if (temp > remainder):
            ret = ret + "0";
        else:
            remainder = remainder - temp;
            ret = ret + "1";
    return int(ret);

def solve(n):
    ret = 0;
    for i in range(0, n):
        if isPalindrome(str(i)) and isPalindrome(str(toBinary(i))):
            ret = ret + i;
    return ret;

print solve(1000000);
