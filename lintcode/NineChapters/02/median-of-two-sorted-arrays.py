__author__ = 'yinjun'

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here

        lenA = len(A)
        lenB = len(B)

        l = lenA + lenB

        if  l%2 == 0 :
            return (self.findKth(A, B, lenA, lenB, 0, 0, l/2) + self.findKth(A, B, lenA, lenB, 0, 0, l/2+1))/2.0
        else:
            return self.findKth(A, B, lenA, lenB, 0, 0, l/2+1)

    def findKth(self, A, B, lenA, lenB, startA, startB, k):
        import  sys
        if startA >= lenA:
            return B[startB + k - 1]
        if startB >= lenB:
            return A[startA + k -1]

        if k == 1:
            return min(A[startA], B[startB])

        indexA = startA + k/2 -1
        if indexA >= lenA :
            nextA = sys.maxint
        else:
            nextA = A[indexA]

        indexB = startB + k/2-1
        if indexB >= lenB:
            nextB = sys.maxint
        else:
            nextB = B[indexB]

        if nextA<nextB:
            return self.findKth(A, B, lenA, lenB, startA + k/2, startB,  k-k/2)
        else:
            return self.findKth(A, B, lenA, lenB, startA, startB + k/2, k-k/2)


s = Solution()
print s.findMedianSortedArrays([1,2,3,4,5,6], [2,3,4,5])