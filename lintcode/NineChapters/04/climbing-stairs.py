__author__ = 'yinjun'

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here

        if n<=2 :
            return n

        stairs = [0 for i in range(n)]

        stairs[0] = 1
        stairs[1] = 2

        for i in range(2, n):
            stairs[i] = stairs[i-1] + stairs[i-2]

        return stairs[n-1]
