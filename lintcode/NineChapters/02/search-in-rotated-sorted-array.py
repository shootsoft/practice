__author__ = 'yinjun'

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here

        length = len(A)

        if length == 0:
            return -1

        start = 0
        end = length - 1

        while start + 1 < end:
            mid = start + (end-start)/2

            if A[mid] == target:
                return mid
            elif A[start] < A[mid]:
                if A[start] <= target and target<=A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target and target<= A[end]:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1


s = Solution()
print s.search([0,1,2,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1], -9)