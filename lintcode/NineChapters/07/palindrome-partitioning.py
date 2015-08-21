__author__ = 'yinjun'

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here

        n = len(s)

        if n == 0:
            return []

        if n == 1:
            return [[n]]

        self.partition_init(s)
        self.partition_help(s, 0, [])

        return self.results

    def partition_help(self, s, start, result):

        if start == len(s):
            self.results.append(result[:])


        for i in range(start+1, len(s)+1):

            if not self.dp[start][i-1]:
                continue
            else:
                sub = s[start:i]
                result.append(sub)
                self.partition_help(s, i, result)
                result.pop()



    def partition_init(self, s):
        n=len(s)

        dp = [[False for j in range(n)] for i  in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(1, n):
            dp[i-1][i] = s[i-1] == s[i]

        for length in range(2, n):
            for start in range(0, n-i):
                dp[start][start+length] = dp[start+1][start+length-1] and s[start] == s[start+length]

        for i in range(n):
            print dp[i]

        self.dp = dp
        self.results = []

s = Solution()
print s.partition("abbab")
#Output
#[["abba","b"],["a","bb","a","b"],["a","b","b","a","b"]]
#Expected
#[["abba","b"],["a","b","bab"],["a","bb","a","b"],["a","b","b","a","b"]]