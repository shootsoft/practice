__author__ = 'yinjun'

#@see http://www.jiuzhang.com/solutions/longest-common-subsequence/
class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here

        x = len(A)
        y = len(B)

        dp = [[0 for j in range(y+1)] for i in range(x+1)]

        for i in range(1, x+1):
            for j in range(1, y+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[x][y]