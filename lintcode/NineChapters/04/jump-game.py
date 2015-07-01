__author__ = 'yinjun'

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if A == None or A == []:
            return False

        n = len(A)

        farest = A[0]

        for i in range(1, n):

            if farest >= i and A[i] + i >= farest:
                farest = A[i] + i

        return farest > n-1



# dynamic programming
# class Solution:
#     # @param A, a list of integers
#     # @return a boolean
#     def canJump(self, A):
#         # write your code here
#
#         if A == None or A == []:
#             return False
#
#         n = len(A)
#
#         jumps = [False for i in range(n)]
#         jumps[0] = True
#
#         for i in range(1, n):
#             for j in range(0, i):
#                 if jumps[j] and j + A[j] >= i:
#                     jumps[i] = True
#                     break
#             print jumps
#
#         return jumps[n-1]

s = Solution()
print s.canJump([4,6,9,5,9,3,0])