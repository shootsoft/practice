class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        if nums == None or nums ==[]:
            return 0
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            
        for k,v in d.items():
            if v == 1:
                return k
        return

#another
# class Solution:
#     # @param {integer[]} nums
#     # @return {integer}
#     def singleNumber(self, nums):
#         z = 0
#         for i in nums:
#             z = z ^ i
#         return z