# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?

def getSolutions(p):
    ret = 0;
    for i in range(1, p):
        if (p * p - 2 * p * i) % (2 * p - 2 * i) == 0:
            ret = ret + 1;
    return ret;

def solve(n):
    best = 0;
    ret = 0;
    for i in range(1, n + 1):
        s = getSolutions(i);
        if s > best:
            best = s;
            ret = i;
    return ret;

print solve(1000);

