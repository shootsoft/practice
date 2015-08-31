__author__ = 'yinjun'

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def totalNQueens(self, n):
        # write your code here
        self.results=0
        self.solve(n, [])
        return self.results

    def solve(self, n, result):

        l = len(result)
        if l == n:
            self.results+=1
            return

        for i in range(0, n):
            if l == 0:
                result.append(i)
            else:
                last = result[l-1]
                if i != last -1 and i != last and i!=last+1:
                    isContinue = False
                    for j in range(l):
                        if result[j] == i:
                            isContinue = True
                            break

                        if abs(j - l) == abs( result[j] - i):
                            #print j, result[j], ' vs ', l, i
                            isContinue = True
                            break

                    if isContinue:
                        continue

                    result.append(i)
                else:
                    continue
            self.solve(n, result)
            result.pop()



