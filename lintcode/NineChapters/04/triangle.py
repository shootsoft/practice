__author__ = 'yinjun'

class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here

        if triangle == None or triangle == []:
            return 0

        n = len(triangle)

        path=[[0 for j in range(n)] for i in range(n)]


        path[0][0] = triangle[0][0]

        for i in range(1, n):
            path[i][0] =path[i-1][0]+ triangle[i][0]

        for i in range(1, n):
            for j in range(1, i+1):

                if i == j:
                    path[i][j] = path[i-1][j-1] + triangle[i][j]
                else:
                    path[i][j] = min(path[i-1][j-1], path[i-1][j]) + triangle[i][j]

        #print path
        return min(path[n-1])


s = Solution()
print s.minimumTotal([[1],[2,3]])






