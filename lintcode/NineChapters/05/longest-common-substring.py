__author__ = 'yinjun'

#ref http://blog.csdn.net/cser_coding/article/details/26097345
class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here

        x = len(A)
        y = len(B)

        if x ==0 or y==0:
            return 0

        dp = [[0 for j in range(y)] for i in range(x)]
        
        max_len=0
        for i in range(x):
            for j in range(y):
                if A[i] == B[j]:

                    if i==0 or j ==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1

                    if dp[i][j]> max_len:
                        max_len = dp[i][j]
        #print dp

        return max_len



s = Solution()
print s.longestCommonSubstring("abc", "a")
print s.longestCommonSubstring("abcd", "ac")