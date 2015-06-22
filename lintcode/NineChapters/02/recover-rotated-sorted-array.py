__author__ = 'yinjun'


class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        length = len(nums)
        minPos = self.findMin(nums, length)

        #print minPos, nums[minPos]
        if minPos > 0:
            self.reverseArray(nums, 0, minPos - 1)
        self.reverseArray(nums, minPos, length - 1)
        self.reverseArray(nums, 0, length - 1)



    def findMin(self, nums, length):

        minPos = 0
        if length > 1:
            for i in range(1, length):
                if nums[i] < nums[minPos]:
                    minPos = i
        return minPos
        # start = 0
        # end = len(nums) - 1
        # #last = end
        #
        # while start + 1 < end:
        #
        #     mid = start + (end - start) / 2
        #
        #     if nums[end] < nums[mid]:
        #         start = mid
        #     elif nums[end] >= nums[mid]:
        #         end = mid
        #
        #
        # if nums[start] < nums[end]:
        #     return start
        # else:
        #     return end

    def reverseArray(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def swap(self,nums, x, y):
        z = nums[x]
        nums[x] = nums[y]
        nums[y] = z


s = Solution()
nums = [4,5, 1,2,3]
s.recoverRotatedSortedArray(nums)
print nums

nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
s.recoverRotatedSortedArray(nums)
print nums

