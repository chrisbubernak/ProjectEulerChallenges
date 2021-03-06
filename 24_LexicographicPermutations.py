#A permutation is an ordered arrangement of objects. For example, 3124 is one possible
#permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed
#numerically or alphabetically, we call it lexicographic order. The lexicographic
#permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6,
#7, 8 and 9?

digits = list('0123456789');
stop = 1000000;

def solve(string, leftOvers):
    if (len(leftOvers) == 0):
        global stop;
        stop = stop - 1;
        if stop == 0:
            return string;
    else:
        leftOvers.sort();
        for i in range(0, len(leftOvers)):
            copy = list(leftOvers);
            copy.remove(leftOvers[i]);
            ret = solve(string+leftOvers[i], copy);
            if (ret):
                return ret;
            
print solve('', digits);
