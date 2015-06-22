__author__ = 'yinjun'



class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeakElement(self, A):
        # write your code here

        start = 0
        length = len(A)
        end = length - 1

        if end < 0:
            return -1

        while start + 1 < end:
            mid = start + (end-start)/2

            if mid - 1 >= 0 and mid + 1 < length:

                if A[mid-1]<A[mid] and A[mid+1]<A[mid]:
                    return mid
                elif A[mid-1] < A[mid] and A[mid] < A[mid+1]:
                    start = mid
                else:
                    end = mid
            else:
                break

        if A[start] > A[end]:
            return start
        else:
            return end