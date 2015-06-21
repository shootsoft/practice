__author__ = 'yinjun'

class Solution:

    def subsetsWithDup(self, num):

        if num == None:
            return
        result = []
        lst = []
        num.sort()
        length = len(num)
        self.subsetHelp(result, lst, length, num, 0)
        return result

    def subsetHelp(self, result, lst, length, num, pos):

        result.append(lst[:])
        for i in range(pos, length):
            if i!=pos and num[i] == num[i - 1]:
                continue
            lst.append(num[i])
            self.subsetHelp(result, lst, length, num, i + 1)
            lst.remove(lst[len(lst)-1])



s = Solution()
print s.subsetsWithDup([1, 2, 2])
