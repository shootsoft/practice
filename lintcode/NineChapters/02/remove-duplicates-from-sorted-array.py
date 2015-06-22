__author__ = 'yinjun'

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here

        if A == None or A==[]:
            return 0
        length = len(A)
        i = 0
        offset = 0

        while i<length-1:

            if A[i] == A[i+1]:
                offset += 1
            else:
                A[i-offset] = A[i]

            i += 1

        A[i-offset] = A[i]

        return length - offset



s = Solution()
A = [1,2, 3, 3, 4]
print s.removeDuplicates(A)
print A