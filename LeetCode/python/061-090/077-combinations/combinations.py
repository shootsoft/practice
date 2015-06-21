__author__ = 'yinjun'


class Solution:

    # @return a list of lists of integers
    def combine(self, n, k):
        self.a = range(k)
        self.ret =[]
        self.build(0, k, n, 1);
        return self.ret


    def build(self, dep, maxDep, n, start):

        if (dep == maxDep):
            self.ret.append(self.a[:])
            return;

        for i in range(start, n+1):
            self.a[dep] = i
            self.build(dep + 1, maxDep,n,i+1)


s = Solution()

print s.combine(7,3)
print [[1,2,3],[1,2,4],[1,2,5],[1,2,6],[1,2,7],[1,3,4],[1,3,5],[1,3,6],[1,3,7],[1,4,5],[1,4,6],[1,4,7],[1,5,6],[1,5,7],[1,6,7],[2,3,4],[2,3,5],[2,3,6],[2,3,7],[2,4,5],[2,4,6],[2,4,7],[2,5,6],[2,5,7],[2,6,7],[3,4,5],[3,4,6],[3,4,7],[3,5,6],[3,5,7],[3,6,7],[4,5,6],[4,5,7],[4,6,7],[5,6,7]]


print s.combine(4,3)
print [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]


print s.combine(4,2)
print [
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

print s.combine(5,3)
print [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]


print s.combine(5,4)
print [[1,2,3,4],[1,2,3,5],[1,2,4,5],[1,3,4,5],[2,3,4,5]]


print s.combine(10, 7)
print [[1,2,3,4,5,6,7],[1,2,3,4,5,6,8],[1,2,3,4,5,6,9],[1,2,3,4,5,6,10],[1,2,3,4,5,7,8],[1,2,3,4,5,7,9],[1,2,3,4,5,7,10],[1,2,3,4,5,8,9],[1,2,3,4,5,8,10],[1,2,3,4,5,9,10],[1,2,3,4,6,7,8],[1,2,3,4,6,7,9],[1,2,3,4,6,7,10],[1,2,3,4,6,8,9],[1,2,3,4,6,8,10],[1,2,3,4,6,9,10],[1,2,3,4,7,8,9],[1,2,3,4,7,8,10],[1,2,3,4,7,9,10],[1,2,3,4,8,9,10],[1,2,3,5,6,7,8],[1,2,3,5,6,7,9],[1,2,3,5,6,7,10],[1,2,3,5,6,8,9],[1,2,3,5,6,8,10],[1,2,3,5,6,9,10],[1,2,3,5,7,8,9],[1,2,3,5,7,8,10],[1,2,3,5,7,9,10],[1,2,3,5,8,9,10],[1,2,3,6,7,8,9],[1,2,3,6,7,8,10],[1,2,3,6,7,9,10],[1,2,3,6,8,9,10],[1,2,3,7,8,9,10],[1,2,4,5,6,7,8],[1,2,4,5,6,7,9],[1,2,4,5,6,7,10],[1,2,4,5,6,8,9],[1,2,4,5,6,8,10],[1,2,4,5,6,9,10],[1,2,4,5,7,8,9],[1,2,4,5,7,8,10],[1,2,4,5,7,9,10],[1,2,4,5,8,9,10],[1,2,4,6,7,8,9],[1,2,4,6,7,8,10],[1,2,4,6,7,9,10],[1,2,4,6,8,9,10],[1,2,4,7,8,9,10],[1,2,5,6,7,8,9],[1,2,5,6,7,8,10],[1,2,5,6,7,9,10],[1,2,5,6,8,9,10],[1,2,5,7,8,9,10],[1,2,6,7,8,9,10],[1,3,4,5,6,7,8],[1,3,4,5,6,7,9],[1,3,4,5,6,7,10],[1,3,4,5,6,8,9],[1,3,4,5,6,8,10],[1,3,4,5,6,9,10],[1,3,4,5,7,8,9],[1,3,4,5,7,8,10],[1,3,4,5,7,9,10],[1,3,4,5,8,9,10],[1,3,4,6,7,8,9],[1,3,4,6,7,8,10],[1,3,4,6,7,9,10],[1,3,4,6,8,9,10],[1,3,4,7,8,9,10],[1,3,5,6,7,8,9],[1,3,5,6,7,8,10],[1,3,5,6,7,9,10],[1,3,5,6,8,9,10],[1,3,5,7,8,9,10],[1,3,6,7,8,9,10],[1,4,5,6,7,8,9],[1,4,5,6,7,8,10],[1,4,5,6,7,9,10],[1,4,5,6,8,9,10],[1,4,5,7,8,9,10],[1,4,6,7,8,9,10],[1,5,6,7,8,9,10],[2,3,4,5,6,7,8],[2,3,4,5,6,7,9],[2,3,4,5,6,7,10],[2,3,4,5,6,8,9],[2,3,4,5,6,8,10],[2,3,4,5,6,9,10],[2,3,4,5,7,8,9],[2,3,4,5,7,8,10],[2,3,4,5,7,9,10],[2,3,4,5,8,9,10],[2,3,4,6,7,8,9],[2,3,4,6,7,8,10],[2,3,4,6,7,9,10],[2,3,4,6,8,9,10],[2,3,4,7,8,9,10],[2,3,5,6,7,8,9],[2,3,5,6,7,8,10],[2,3,5,6,7,9,10],[2,3,5,6,8,9,10],[2,3,5,7,8,9,10],[2,3,6,7,8,9,10],[2,4,5,6,7,8,9],[2,4,5,6,7,8,10],[2,4,5,6,7,9,10],[2,4,5,6,8,9,10],[2,4,5,7,8,9,10],[2,4,6,7,8,9,10],[2,5,6,7,8,9,10],[3,4,5,6,7,8,9],[3,4,5,6,7,8,10],[3,4,5,6,7,9,10],[3,4,5,6,8,9,10],[3,4,5,7,8,9,10],[3,4,6,7,8,9,10],[3,5,6,7,8,9,10],[4,5,6,7,8,9,10]]
