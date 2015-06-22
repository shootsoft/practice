__author__ = 'yinjun'

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here

        length = len(A)
        start = 0
        end = length - 1

        if end < 0:
            return [-1,-1]

        while start + 1 < end:

            mid = start + (end - start) /2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start]!=target and A[end]!=target:
            return[-1, -1]

        if A[start] == target and A[end] == target:
            pos1 = min(start, end)
        elif A[end] == target:
            pos1 = end
        elif A[start] == target:
            pos1 = start

        start = 0
        end = length - 1

        while start + 1 < end:

            mid = start + (end - start) /2

            if A[mid] > target:
                end = mid
            else:
                start = mid

        if A[start] == target and A[end] == target:
            pos2 = max(start, end)
        elif A[end] == target:
            pos2 = end
        elif A[start] == target:
            pos2 = start

        return [pos1, pos2]

s= Solution()
print s.searchRange([9,10,100,101,1002,10203], 10203)
