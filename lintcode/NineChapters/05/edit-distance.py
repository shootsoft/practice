__author__ = 'yinjun'

class Solution:
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        n = len(word1)
        m = len(word2)

        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        #print dp

        for i in range(m+1):
            dp[0][i] = i

        for j in range(n+1):
            dp[j][0] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] =  dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return dp[n][m]


s = Solution()
print s.minDistance("word1", "word2word")