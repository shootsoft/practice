__author__ = 'yinjun'


class Solution:

    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        self.result = []
        cur = []
        A.sort()
        length = len(A)
        if k == 1:
            for i in range(length):
                if A[i] == target:
                    self.result.append([A[i]])
        else:
            self.KSumHelp(A, k, target, 0, length , cur)
        return len(self.result)



    def KSumHelp(self, A, k, target, start, length, cur):
        print k, target
        if k == 2:
            i = start
            j = length -1
            while i < j:
                two = A[i] + A[j]
                if two == target:
                    cur.append(A[i])
                    cur.append(A[j])
                    self.result.append(cur[:])
                    cur.pop()
                    cur.pop()
                    i += 1
                elif two > target:
                    j -= 1
                else:
                    i += 1

        else:

            for i in range(start, length):
                if i > start and A[i] == A[i - 1]:
                    continue
                #print 'before', cur
                cur.append(A[i])
                self.KSumHelp(A, k-1, target - A[i], i + 1, length, cur )
                #print 'after', cur
                cur.pop()


##DP C++ for online test
# class Solution {
# public:
#     int ans[105][1005];
#     int kSum(vector<int> A, int K, int target) {
#         ans[0][0] = 1;
#         for(int i = 0; i < A.size(); ++i)
#             for(int j = K; j > 0; j--)
#                 for(int k = target; k >= A[i]; k--) {
#                     ans[j][k] += ans[j - 1][k - A[i]];
#                     if(ans[j][k] > 2147483647)
#                         return -1;
#                 }
#         return ans[K][target];
#     }
# };


#DP python
# class Solution:
#
#     def kSum(self, A, k, target):
#         ans = [[[0 for i in range(target + 1)] for j in range(k + 1)] for K in range(len(A) + 1)]
#
#         ans[0][0][0] = 1
#         for I in range(len(A)):
#             item = A[I]
#             for J in range(target + 1):
#                 for K in range(k + 1):
#                     tk = k - K
#                     tj = target - J
#                     ans[I + 1][tk][tj] = ans[I][tk][tj]
#                     if tk - 1 >= 0 and tj - item >= 0:
#                         ans[I + 1][tk][tj] += ans[I][tk - 1][tj - item]
#         return ans[len(A)][k][target]

s = Solution()
print s.kSum([1,2,3,4], 2, 5)

print s.kSum([1,4,7,10,12,15,16,18,21,23,24,25,26,29], 5, 113)
print s.kSum([1,3,4,5,8,10,11,12,14,17,20,22,24,25,28,30,31,34,35,37,38,40,42,44,45,48,51,54,56,59,60,61,63,66], 24, 842)