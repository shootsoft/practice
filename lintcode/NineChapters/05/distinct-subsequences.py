__author__ = 'yinjun'

#ref http://blog.csdn.net/abcbc/article/details/8978146

class Solution:
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here

        t = len(T)
        s = len(S)

        if s == t and s == 0:
            return 1

        dp = [[0 for j in range(s+1)] for  i in range(t+1)]

        dp[0][0] = 1

        for j in range(1, s+1):
            dp[0][j] = 1

        for i in range(1, t+1):
            dp[i][0] = 0

        for i in range(1, t+1):
            for j in range(1, s+1):
                dp[i][j] = dp[i][j - 1]

                if T[i-1] == S[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        #print dp

        return dp[t][s]


s = Solution()
print s.numDistinct("ddd", "dd")