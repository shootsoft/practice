class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        nums = range(1, 10)
        self.results = []
        self.combination(nums, n, k, 0, [])
        return self.results


    def combination(self, nums, target, k, start, result):

        if k <= 0 :
            return
        elif k == 1:
            for i in nums:
                if i == target:
                    self.results.append([i])
        elif k == 2:

            end = len(nums) - 1

            while start < end:
                s = nums[start] + nums[end]
                if s == target:
                    result.append(nums[start])
                    result.append(nums[end])
                    self.results.append(result[:])
                    result.pop()
                    result.pop()
                    start += 1
                elif s < target:
                    start += 1
                else:
                    #s > target
                    end -= 1

        else:

            for i in range(start, len(nums)-1):
                t = target - nums[i]
                if t >= nums[i+1]:
                    result.append(nums[i])
                    self.combination(nums, t, k -1, i + 1, result )
                    result.pop()
                else:
                    break