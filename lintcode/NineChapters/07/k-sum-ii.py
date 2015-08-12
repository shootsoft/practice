__author__ = 'yinjun'

class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        A.sort()
        self.results=[]

        self.kSum(A, k, target, 0, [])
        return self.results

    def kSum(self, A, k, target, start, result):

        if k == 1:
            for i in A:
                if i == target:
                    self.results.append([i])
        elif k == 2:

            i = start
            j = len(A)-1

            while i < j:
                s = A[i] + A[j]
                if s ==target:
                    result.append(A[i])
                    result.append(A[j])
                    self.results.append(result[:])
                    result.pop()
                    result.pop()
                    i += 1
                elif s > target:
                    j -= 1
                else:
                    i += 1
        else:

            for i in range(start, len(A)):
                result.append(A[i])
                self.kSum(A, k-1, target- A[i], i+1, result)
                result.pop()


