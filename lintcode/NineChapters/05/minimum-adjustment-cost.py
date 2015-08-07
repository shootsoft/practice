__author__ = 'yinjun'

#@see http://www.cnblogs.com/yuzhangcmu/p/4153927.html
class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        # write your code here
        import sys
        MAX = 100
        size = len(A)
        dp = [[sys.maxint for j in range(MAX+1)] for i in range(size)]

        for i in range(size):
            for j in range(1, MAX+1):
                if i ==0:
                    dp[i][j] = abs(j - A[i])
                else:

                    for k in range(1, MAX+1):
                        if abs(j-k)> target:
                            continue
                        dp[i][j] = min(dp[i][j], (abs(j-A[i])+ dp[i-1][k]))

            #break

        #print dp[size-1]
        return min(dp[size-1])


s = Solution()
print s.MinAdjustmentCost([1,4,2,3], 1)