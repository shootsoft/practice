__author__ = 'yinjun'

class Solution:

    def jump(self, A):

        if A==None or A == []:
            return 0

        n = len(A)
        steps = [0 for i in range(n)]

        start = 0
        end = 0
        jumps = 0
        while end < n-1:

            jumps += 1
            farthest = end

            for i in range(start, end + 1):
                if A[i] + i > farthest:
                    farthest = A[i] + i

            start = end + 1
            end = farthest

        return jumps

# class Solution:
#     # @param A, a list of integers
#     # @return an integer
#     def jump(self, A):
#         import sys
#         # write your code here
#
#         if A==None or A == []:
#             return 0
#
#         n = len(A)
#         steps = [0 for i in range(n)]
#
#         steps[0] = 0
#
#         for i in range(1, n):
#             steps[i] = sys.maxint
#             for j in range(0, i):
#                 if steps[j] != sys.maxint and j + A[j] >= i:
#                     steps[i] = steps[j] + 1
#                     break
#
#         return steps[n-1]
