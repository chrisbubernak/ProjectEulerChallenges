#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?

def solve(n):
    x = 1
    for i in range(0, n):
        x = x*2
        x = str(x)
        i = x.__len__() - 1
        while x[i] == 0:
            x = x[:-1]
        x = int(x) 
        
    sum = 0
    x = str(x)
    for i in x:
        sum += int(i)
    return sum

print solve(1000)
