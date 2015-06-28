__author__ = 'yinjun'

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here

        if root == None:
            return True

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        
        if left>-1 and right >-1:
            return abs(left-right) <= 1
        else:
            return False


    def getHeight(self, root):

        if root == None:
            return 0

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        
        if left == -1 or right == -1:
            return -1
        elif abs(left-right) <= 1:
            return max(left, right) + 1
        else:
            return -1