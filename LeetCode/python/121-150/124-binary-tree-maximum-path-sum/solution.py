__author__ = 'yinjun'

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here

        singlePath, sumPath = self.help(root)
        return sumPath

    def help(self, root):
        import  sys
        if root == None:
            return 0, -1 * sys.maxint

        leftSingle, leftSum = self.help(root.left)
        rightSingle, rightSum = self.help(root.right)

        singlePath = max(leftSingle, rightSingle) + root.val
        singlePath = max(0, singlePath)

        sumPath = max(leftSum, rightSum)
        sumPath = max(sumPath, leftSingle + rightSingle + root.val)

        return singlePath, sumPath

