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
            elif A[start] > A[end]:
                if A[mid] < A[start]  and target > A[mid]  or A[mid]> A[start] and (target< A[start] or target>A[mid]):
                    start = mid
                else:
                    #print 'else'
                    end = mid
            elif A[start] < A[end] and A[mid] < target:
                end = mid
            else:
                start = mid

        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1


s = Solution()
print s.search([0,1,2,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1], -9)