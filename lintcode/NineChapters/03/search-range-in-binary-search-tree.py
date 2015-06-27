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
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        self.result = []
        self.collectNodes(root, k1, k2)
        self.result.sort()
        return self.result

    def collectNodes(self, root, k1, k2):

        if root == None:
            return

        if root.val>=k1 and root.val<=k2:
            self.result.append(root.val)

        self.collectNodes(root.left, k1, k2)
        self.collectNodes(root.right, k1, k2)