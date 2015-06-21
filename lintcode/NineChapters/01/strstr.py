__author__ = 'yinjun'

class Solution:

    def strStr(self, source, target):
        # write your code here

        if source == None or target == None:
            return -1
        
        if source == target:
            return 0
        
        ls = len(source)
        lt = len(target)

        if lt >= ls:
            return -1

        for i in range(ls-lt):
            exit = True
            for j in range(lt):
                if target[j] != source[j+i]:
                    exit = False
                else:
                    continue

            if exit == True:
                return i

        return -1


