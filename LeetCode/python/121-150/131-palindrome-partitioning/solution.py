__author__ = 'yinjun'

class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):

        l = len(s)
        r = self.getPalindrome(s, l)
        p = []
        c = []

        print r

        self.getCut(s, r, l, p, c, 0)

        return p

    def getCut(self, s, r, l, p, c, start):


        if start ==l:
            p.append(c[:])


        for i in range(start, l):
            if r[start][i]:
                c.append(s[start:i+1])
                self.getCut(s, r, l, p, c, i + 1)
                c.pop()








    def getPalindrome(self, s, l):

        r = [[False for i in range(l)] for j in range(l)]

        for i in range(l):
            r[i][i] = True

        for i in range(l-1):
            r[i][i+1] = s[i] == s[i+1]


        for length in range(2, l):
            for start in range(0, l-length):
                r[start][start+length] = r[start+1][start+length-1] and s[start] == s[start+length]

        return r

