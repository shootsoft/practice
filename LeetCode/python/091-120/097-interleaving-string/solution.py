__author__ = 'yinjun'

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l3!=l1+l2:
            return False

        dp = [[False for j in range(l2+1)] for i in range(l1+1)]

        dp[0][0] = True

        for i in range(1, l1+1):
            if s3[i-1] == s1[i-1] and dp[i-1][0]:
                dp[i][0] = True

        for j in range(1, l2+1):
            if s3[j-1] == s2[j-1] and dp[0][j-1]:
                dp[0][j] = True

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if s3[i+j-1] == s1[i-1] and dp[i-1][j] or s3[i+j-1]==s2[j-1] and dp[i][j-1]:
                    dp[i][j] = True

        return dp[l1][l2]