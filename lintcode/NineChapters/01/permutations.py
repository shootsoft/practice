__author__ = 'yinjun'

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here

        if nums == None:
            return []

        result = []
        lst = []
        length = len(nums)

        self.permuteHelp(result, lst, length, nums)

        return result


    def permuteHelp(self, result, lst, length, nums):

        if len(lst) == length:
            result.append(lst[:])
            return

        for i in range(0, length):
            if nums[i] in lst:
                continue
            lst.append(nums[i])
            self.permuteHelp(result, lst, length, nums)
            lst.pop()


s = Solution()
print s.permute([1,2,3,4])