__author__ = 'yinjun'

class VersionControl:

    @classmethod
    def isBadVersion(cls, id):
        return False
#class VersionControl:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionControl.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here

        start = 1
        end = n

        while start + 1 < end:
            mid = start + (end - start)/2

            v = VersionControl.isBadVersion(mid)

            if v:
                end = mid
            else:
                start = mid

        if start < end:
            if VersionControl.isBadVersion(start):
                return start
            else:
                return end
        else:
            if VersionControl.isBadVersion(end):
                return end
            else:
                return start