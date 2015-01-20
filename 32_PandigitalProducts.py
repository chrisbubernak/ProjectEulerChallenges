# We shall say that an n-digit number is pandigital if it makes use
# of all the digits 1 to n exactly once; for example, the 5-digit
# number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 3 x 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9
# pandigital.

# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be
# sure to only include it once in your sum.

import math;

def pandigital(usedDigits):
    digits = "123456789";

    if "0" in usedDigits:
        return False;
    
    for i in range(0, len(digits)):
        if digits[i] not in usedDigits:
            return False;
        
    return True;
        
def solve(n):
    products = {};
    ret = 0;
    maxNum = int(math.pow(10, math.floor(n/2.0) - 1)) * n;
    for i in range(0, maxNum):
        for j in range(0, maxNum):
            k = i * j;
            usedDigits = str(i) + str(j) + str(k);
            if len(usedDigits) > 9:
                break;
            if pandigital(usedDigits) and k not in products.keys():
                products[k] = True;
                ret = ret + k;
    return ret;
print solve(9);
