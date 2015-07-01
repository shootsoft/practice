__author__ = 'yinjun'

__author__ = 'yinjun'

class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here

        if obstacleGrid == None or obstacleGrid==[]:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        path = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            else:
                path[i][0] = 1

        for j in range(m):
            if obstacleGrid[0][j] == 1:
                break
            else:
                path[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    path[i][j] = 0
                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]

        return path[n-1][m-1]