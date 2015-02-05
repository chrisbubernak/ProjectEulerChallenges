# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?

def getSolutions2(p):
    ret = 0;
    for i in range(2, p):
        for j in range(p - (2 * i), 1, -1):
            k = p - i - j;
            if j > k:
                break;
            k2 = k * k;
            i2 = i * i;
            j2 = j * j;
            if (k2 > (i2 + j2)):
                break;
            if k2 == (i2 + j2):
                ret = ret + 1;
                break;
    return ret;

def solve(n):
    best = 0;
    ret = 0;
    for i in range(1, n + 1):
        s = getSolutions2(i);
        if s > best:
            best = s;
            ret = i;
    return ret;

print solve(1000);
