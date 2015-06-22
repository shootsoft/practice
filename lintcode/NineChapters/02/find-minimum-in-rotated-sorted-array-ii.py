__author__ = 'yinjun'

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here

        start = 0
        end = len(num) - 1

        while start < end:
            mid = (start + end) / 2

            if num[mid]> num[end]:
                start = mid + 1
            elif num[mid] < num[end]:
                end = mid
            else:
                end = end-1

        return num[start]

