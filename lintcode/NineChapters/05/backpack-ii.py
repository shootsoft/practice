__author__ = 'yinjun'

'''
@see http://www.cnblogs.com/EdwardLiu/p/4272300.html
@see http://simpleandstupid.com/2014/12/21/backpack-ii-lintcode/
'''
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here

        l = len(A)

        dp = [[0 for j in range(m+1)] for i in range(l+1)]

        for i in range(1, l+1):
            for j in range(0, m+1):

                if j-A[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] + V[i-1])

        return dp[l][m]
