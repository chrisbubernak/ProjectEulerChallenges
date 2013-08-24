# -*- coding: utf-8 -*-
def next(x):
    if x%2 == 0:
        return x/2;
    return 3*x+1;
#The following iterative sequence is defined for the set of positive integers:

#n -> n/2 (n is even)
#n -> 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

num = 1000000;
cache = [None]*num;
cache[1] = 1;
best = 0;
bestIndex = 0;
for i in range(1,num):
    count = 0;
    x = i;
    while (x != 1 and x>=i):
        if (x%2 == 0):
            x = x/2;
        else:
            x =  3*x+1;
        count = count + 1;
    count = count + cache[x];
    if count > best:
        bestIndex = i;
        best = count;
    cache[i] = count;
print "Chain of length " + str(best) +" originates from " + str(bestIndex) + " and is the longest chain originating from numbers under " + str(num);


        
