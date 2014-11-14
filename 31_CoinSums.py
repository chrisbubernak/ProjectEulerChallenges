#In England the currency is made up of pound, and pence, and
#there are eight coins in general circulation:

#1p, 2p, 5p, 10p, 20p, 50p, p1 (100p) and p2 (200p).
#It is possible to make p2 in the following way:

#1*p1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
#How many different ways can p2 be made using any number of coins?

def solve(n, coins):
    count = 0;
    for i in range(0, len(coins)):
        coin = len(coins) - i - 1;
        val = coins[coin];
        remainder = n - val;
        if remainder == 0:
            count = count + 1;
        elif remainder > 0:
            count = count + solve(remainder, coins[0:coin+1])
    return count;

print solve(200, [1,2,5,10,20,50,100,200]);
