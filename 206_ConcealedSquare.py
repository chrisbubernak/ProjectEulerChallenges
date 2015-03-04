# Find the unique positive integer whose square has the form
# 1_2_3_4_5_6_7_8_9_0,
# where each "_" is a single digit.

import math;

def matchesPattern(n):
    nStr = str(n);
    if len(nStr) != 19:
        return False;
    for i in range(0, 9):
        if nStr[i * 2] != str(i + 1):
            return False;
    return nStr[18] == "0";

def solve():
    maxNum = int(math.ceil(math.sqrt(1929394959697989990)));
    minNum = int(math.ceil(math.sqrt(1020304050607080900)));
    cur = maxNum;
    while cur >= minNum:
        if matchesPattern(cur * cur):
            return cur;
        else:
            cur = cur - 1;

print solve();
