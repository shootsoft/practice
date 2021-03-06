__author__ = 'yinjun'

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        self.results = []
        candidates.sort()
        self.combination(candidates, target, 0, [])
        return self.results

    def combination(self, candidates, target, start, result):

        if target == 0 :
            self.results.append(result[:])
        elif target > 0 :
            
            for i in range(start, len(candidates)):
                result.append(candidates[i])
                self.combination(candidates,  target - candidates[i], i , result)
                result.pop()
                