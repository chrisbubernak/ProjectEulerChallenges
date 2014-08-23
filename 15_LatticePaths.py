#Starting in the top left corner of a 2x2 grid, and only being able to move to
#the right and down, there are exactly 6 routes to the bottom right corner.

#How many such routes are there through a 20x20 grid?

def solve(n):
    n = (n+1)
    grid = [0] * (n*n)
    
    #initialize the top row and first col
    for i in range(0, n*n):
         if (i < n or i%n ==0):
             grid[i] = 1;
             
    #fill in the rest 
    for i in range(0, n*n):
        if (grid[i] == 0):
            grid[i] = grid[i-1] + grid[i - n];
            
    return grid[n*n-1];
    
print solve(20)