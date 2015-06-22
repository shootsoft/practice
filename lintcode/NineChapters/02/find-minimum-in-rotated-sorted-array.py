__author__ = 'yinjun'

class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here

        start = 0
        length = len(num)
        end = length - 1

        while start + 1 < end:
            mid = start + (end - start) /2

            if mid - 1 >= 0 and mid + 1 < length:

                if num[mid] < num[mid -1] and num[mid] < num[mid+1]:
                    return num[mid]
                elif num[start] > num[end]:
                    if num[mid] > num[start]:
                        start = mid
                    else:
                        end = mid
                else:
                    if num[mid] > num[start]:
                        end = mid
                    else:
                        start = mid
            else:
                break

        return min(num[start], num[end])



s = Solution()
print s.findMin([4, 5, 6, 7, 0, 1, 2])



