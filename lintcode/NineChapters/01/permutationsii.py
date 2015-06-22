__author__ = 'yinjun'

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permuteUnique(self, nums):
        # write your code here

        if nums == None:
            return []

        result = []
        lst = []
        length = len(nums)
        visited = [0 for x in range(length)]
        nums.sort()
        self.permuteHelp(result, lst, visited, length, nums)

        return result


    def permuteHelp(self, result, lst, visited, length, nums):

        if len(lst) == length:
            result.append(lst[:])
            return

        for i in range(0, length):
            if visited[i] == 1 or (i > 0 and nums[i] == nums[i-1] and visited[i-1] == 0):
                continue
            visited[i] = 1
            lst.append(nums[i])
            self.permuteHelp(result, lst, visited, length, nums)
            lst.pop()
            visited[i] = 0


s = Solution()
print s.permuteUnique([1,2,2,4])