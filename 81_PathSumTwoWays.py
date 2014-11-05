#In the 5 by 5 matrix below, the minimal path sum from the top left to the
#bottom right, by only moving to the right and down, is indicated in bold
#red and is equal to 2427.

#131 673 234 103  18
#201  96 342 965 150
#630 803 746 422 111
#537 699 497 121 956
#805 732 524  37 331

#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target
#As..."), a 31K text file containing a 80 by 80 matrix, from the top left to
#the bottom right by only moving right and down.

import math;

def up(index, size):
    if (index - size < 0):
        return -1;
    return index - size;

def left(index, size):
    if (index ) % size == 0:
        return - 1;
    return index - 1;

def solve(matrix):
    size = int(math.sqrt(len(matrix)));
    for i in range(0, len(matrix)):
        l = left(i, size);
        u = up(i, size);
        if (l == -1 and u != -1):
            matrix[i] = int(matrix[i]) + int(matrix[u]);
        elif (u == -1 and l != -1):
            matrix[i] = int(matrix[i]) + int(matrix[l]);
        elif (u != -1 and l != -1):
            matrix[i] = int(matrix[i]) + min(int(matrix[l]), int(matrix[u]));
        else:
            matrix[i] = int(matrix[i]);
    return matrix[len(matrix)-1];

with open ("matrix.txt", "r") as myFile:
    numbers = myFile.read().replace("\n", ",");
    numbers = numbers.split(",");
    numbers = numbers[:-1];
    print solve(numbers);
