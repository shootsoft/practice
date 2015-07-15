__author__ = 'yinjun'

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        dict={}
        max=100
        i=0
        while i<=max:
            if n in dict:
                return False
            else:
                dict[n]=1

                s = list( str(n) )

                x =0
                for m in s:
                    x += int(m)**2

                if x == 1:
                    return True

                n = x
            i+=1
        return False