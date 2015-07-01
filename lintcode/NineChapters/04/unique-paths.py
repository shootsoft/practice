__author__ = 'yinjun'

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        # write your code here

        if m <=1 or n<=1:
            return 1

        path = [[1 for j in range(m)] for i in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                path[i][j] = path[i-1][j] + path[i][j-1]

        return path[n-1][m-1]