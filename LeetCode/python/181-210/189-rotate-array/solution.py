class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):

        length = len(nums)
        pos = length - k % length

        if pos > 0:
            self.reverseArray(nums, 0, pos - 1)
        self.reverseArray(nums, pos, length -1)
        self.reverseArray(nums, 0, length -1)



    def reverseArray(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def swap(self,nums, x, y):
        z = nums[x]
        nums[x] = nums[y]
        nums[y] = z
