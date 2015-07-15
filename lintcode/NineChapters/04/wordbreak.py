__author__ = 'yinjun'

class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        if dict == {} :
            return s == ""
        maxLength = max([len(k) for k,v in dict.items()])
        length = len(s)
        canBreak = [True for i in range(length+1)]
        for i in range(1, length + 1):

            canBreak[i] = False

            for j in range(1, maxLength+1):

                if j>i:
                    break

                if(canBreak[i-j] == False):
                    continue

                w = s[i-j:i]

                if(w in dict):
                    canBreak[i] = True
                    break

        return canBreak[length]

s = Solution()
print s.wordBreak("a", {"a":1} )