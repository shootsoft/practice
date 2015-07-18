class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):

        if p == s:
            return True
        elif p == None or p == "":
            return False

        ls = len(s)
        lp = len(p)

        last_s = 0
        last_p = -1

        i = j = 0

        while i < ls:

            if  j< lp and (p[j] == "?" or s[i] == p[j]):
                i += 1
                j += 1
            elif j < lp and p[j] == "*":
                last_s = i
                last_p = j
                j += 1
            elif last_p >=0:
                last_s += 1
                i = last_s
                j = last_p
            else:
                return False

        if i< ls:
            return False

        while j<lp and p[j] == "*":
            j += 1

        return j == lp

