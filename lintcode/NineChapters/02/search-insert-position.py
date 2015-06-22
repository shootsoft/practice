__author__ = 'yinjun'

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here

        start = 0
        end = len(A) - 1

        if end < 0:
            return 0

        if target <= A[start]:
            return start

        if target > A[end]:
            return end + 1


        while start + 1 < end:

            mid = start + (end - start)/2

            print start, end, mid

            if A[mid] == target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid


        if start < end and A[start] >= target:
            return start
        elif A[end] >= target:
            return end


s = Solution()
print s.searchInsert([1,3,5,6,8,9], 7)