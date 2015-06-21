__author__ = 'yinjun'

class Solution:

    def subsets(self, num):

        if num == None:
            return None
        result = []
        lst = []
        num.sort()
        length = len(num)
        self.subsetHelp(result, lst, length, num, 0)
        return result

    def subsetHelp(self, result, lst, length, num, pos):
        result.append(lst[:])
        for i in range(pos, length):
            # add this will be correct answer
            #if lst !=[] and num[i] <= lst[len(lst)-1]:
            #    continue
            lst.append(num[i])
            self.subsetHelp(result, lst, length, num, i + 1)
            lst.pop()


s = Solution()
print s.subsets([1,2, 3])
