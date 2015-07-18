__author__ = 'yinjun'

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        if s == None or s =="":
            return 0

        l = len(s)
        r = self.getAllPalindrome(s, l)

        f = [0 for i in range(l+1)]

        for i in range(l+1):
            f[i] = i -1

        for i in range(1, l+1):
            for j in range(0, i):
                if r[j][i-1]:
                    f[i] = min(f[i], f[j]+1)

        return f[l]


    def getAllPalindrome(self, s, l):

        r = [[False for i in range(l)] for j in range(l)]

        for i in range(l):
            r[i][i] = True

        for i in range(l-1):
            r[i][i+1] = s[i] == s[i+1]


        for length in range(2, l):
            for start in range(0, l-length):
                r[start][start+length] = \
                        r[start + 1][start + length - 1] and s[start] == s[start + length];

        return r



s = Solution()
print s.getAllPalindrome("aabbccbbaa")
