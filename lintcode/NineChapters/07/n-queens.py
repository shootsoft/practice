__author__ = 'yinjun'

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        self.results=[]
        self.solve(n, 0, [])
        return self.results

    def solve(self, n, start, result):

        if len(result) == n:
            self.results.append(self.convert(result, n))

        for i in range(start, n):
            if i > 0:
                result.append(i)


    def convert(self, result, n):
        r = []
        for i in result:
            cur = []
            for j in range(n):
                if i == j:
                    cur.append('Q')
                else:
                    cur.append('.')
            r.append(cur)
        return r




