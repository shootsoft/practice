__author__ = 'yinjun'

'''
@see http://www.cnblogs.com/lishiblog/p/4183806.html
@see http://www.jiuzhang.com/solutions/backpack/
'''
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        if A ==None or A ==[]:
            return 0

        l = len(A)
        d = [False for i in range(m+1)]
        d[0] = True
        for i in range(1, l+1):
            for j in range(m, -1, -1):
                if j - A[i-1] >=0 and d[j-A[i-1]]:
                    d[j] = d[j-A[i-1]]


        for i in range(m, -1, -1):
            if d[i]:
                return i

        return 0

s = Solution()
print s.backPack(80000, [81,112,609,341,164,601,97,709,944,828,627,730,460,523,643,901,602,508,401,442,738,443,555,471,97,644,184,964,418,492,920,897,99,711,916,178,189,202,72,692,86,716,588,297,512,605,209,100,107,938,246,251,921,767,825,133,465,224,807,455,179,436,201,842,325,694,132,891,973,107,284,203,272,538,137,248,329,234,175,108,745,708,453,101,823,937,639,485,524,660,873,367,153,191,756,162,50,267,166,996,552,675,383,615,985,339,868,393,178,932])
