#n! means n x (n − 1) x ... x 3 x 2 x 1

#For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!

def solve(n):
    x = 1
    j = 1
    for i in range(0, n):
        x = x*j
        x = str(x)
        # strip the trailing 0s off the back of the number
        i = x.__len__() - 1
        while x[i] == 0:
            x = x[:-1]
        x = int(x) 
        j = j+1
    # find the sum
    sum = 0
    x = str(x)
    for i in x:
        sum += int(i)
    return sum

print solve(100)
