__author__ = 'yinjun'

class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here

        if nums == None or nums == []:
            return 0

        l = len(nums)

        length = [0 for i in range()]

        maxLength = 0

        for i in range(l):
            length[i] = 1
            for j in range(0, i):
                if nums[j] <= nums[i]:
                    length[i] = max(length[i], length[j] + 1)

            maxLength = max(maxLength, length[i])

        return maxLength