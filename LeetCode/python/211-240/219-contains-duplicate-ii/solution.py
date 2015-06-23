__author__ = 'yinjun'

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = dict()
        if nums == None or nums == []:
            return False
        for i in range(len(nums)):

            if nums[i] in d and i-d[nums[i]] <= k:
                    return True

            d[nums[i]] = i


        return False