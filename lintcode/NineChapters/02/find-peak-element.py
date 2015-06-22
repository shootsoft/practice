__author__ = 'yinjun'

class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here

        start = 0
        end = len(A) - 1

        while start + 1 <