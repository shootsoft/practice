__author__ = 'yinjun'


class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def merge(self, A, m, B, n):
        # write your code here

        if A == None or B == None or A ==[] or B==[]:
            return


        for i in range(m-1, -1, -1):
            A[i+n] = A[i]
        #print A

        i = n
        j = 0
        p = 0

        while i<m+n and j < n:
            #print i, j
            if A[i] < B[j]:
                A[p] = A[i]
                i += 1
            else:
                A[p] = B[j]
                j += 1
            p += 1
        #print A
        while j < n:
            A[p] = B[j]
            j += 1
            p += 1


s = Solution()
A = [1, 2, 4, 0, 0]
s.mergeSortedArray(A, 3, [3,5], 2)
print A

A = [1, 2, 3, 0, 0]
s.mergeSortedArray(A, 3, [4,5], 2)
print A