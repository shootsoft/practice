__author__ = 'yinjun'

class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here

        if A == None and B== None:
            return None
        elif A == None or A ==[]:
            return B
        elif B == None or B ==[]:
            return A

        i = 0
        j = 0

        lena = len(A)
        lenb = len(B)

        C = [0 for x in range(lena+lenb)]
        p = 0

        while i < lena and j < lenb:

            if A[i] <= B[j]:
                C[p] = A[i]
                i += 1

            elif A[i] > B[j]:
                C[p] = B[j]
                j += 1

            p += 1

        while i<lena:
            C[p] = A[i]
            i += 1
            p += 1

        while j<lenb:
            C[p] = B[j]
            j += 1
            p += 1

        return C




