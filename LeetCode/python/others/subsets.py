__author__ = 'yinjun'

class Subsets:

    def subset(self, num):

        if num == None:
            return
        result = []
        num.sort()
        length = len(num)
        self.subsetHelp(result, length, num, 0)


    def subsetHelp(self, result, length, num, pos):

        print result

        print pos, length, range(pos, length)
        for i in range(pos, length):
            print 'i=', i
            result.append(num[i])
            self.subsetHelp(result, length, num, pos + 1)
            print 'before', result
            result.pop(len(result) - 1)
            print 'after', result


s = Subsets()
s.subset([0,1,2])