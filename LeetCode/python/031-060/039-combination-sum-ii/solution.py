class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        self.results = []
        candidates.sort()
        self.combination(candidates, target, 0, [])
        return self.results


    def combination(self,candidates, target, start, result):
        if target == 0 :
            self.results.append(result[:])
        elif target > 0:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                result.append(candidates[i])
                self.combination(candidates, target-candidates[i], i + 1, result)
                result.pop()