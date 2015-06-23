class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        d = dict()
        if nums == None or nums==[]:
            return False
        l = len(nums)
        for i in range(l):
            if nums[i] in d:
                return True
            else:
                d[nums[i]] = i
        return False
        
        