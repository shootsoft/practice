__author__ = 'yinjun'
class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here

        if grid == None or grid == [] :
            return

        n = len(grid)
        m = len(grid[0])



        sumgrid = [[0 for j in range(m)] for i in range(n)]

        sumgrid[0][0] = grid[0][0]
        for i in range(1, n):
            sumgrid[i][0] = grid[i][0] +  sumgrid[i-1][0]

        for i in range(1, m):
            sumgrid[0][i] = grid[0][i] + sumgrid[0][i-1]

        for i in range(1, n):
            for j in range(1, m):
                sumgrid[i][j] = min(sumgrid[i-1][j], sumgrid[i][j-1]) + grid[i][j]

        #print sumgrid
        return sumgrid[n-1][m-1]