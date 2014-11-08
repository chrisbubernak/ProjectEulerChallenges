#Starting with the number 1 and moving to the right in a clockwise direction
#a 5 by 5 spiral is formed as follows:

#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#It can be verified that the sum of the numbers on the diagonals is 101.

#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
#formed in the same way?

def solve(n):
    ret = 1;
    cur = 1;
    size = 1;
    i = 1;
    while size < n:
        bottomRight = cur + 2 * i;
        bottomLeft = cur + 4 * i;
        topLeft = cur + 6 * i;
        topRight = cur + 8 * i;
        cur = topRight
        ret = ret + bottomRight + bottomLeft + topLeft + topRight;
        i = i + 1;
        size = size + 2;
    return ret;

print solve(1001);
