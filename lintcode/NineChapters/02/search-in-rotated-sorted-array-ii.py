__author__ = 'yinjun'

class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here

        start = 0
        end = len(A) - 1

        while start<end:

            mid = (start+end)/2

            if A[mid] == target:
                return mid

            if A[mid] < A[end]:

                if A[mid] > target and target <= A[end]:
                    end = mid
                else:
                    start = mid+1


            elif A[mid] > A[end]:

                if A[mid] > target and target>= A[end]:
                    start = mid + 1
                else:
                    end = mid
            else:
                end = end-1

        if A[start]==target:
            return start
        else:
            return False