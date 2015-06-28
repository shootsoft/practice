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
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if preorder ==[] and inorder == []:
            return None

        root = TreeNode(preorder[0])

        inpos = inorder.index(preorder[0])

        if inpos>0:
            left_pre = preorder[1:inpos+1]
            left_in = inorder[0:inpos]
            root.left = self.buildTree(left_pre, left_in)

        length = len(inorder)

        if  inpos + 1 < length:

            right_pre = preorder[inpos+1:]
            right_in = inorder[inpos+1:]
            root.right = self.buildTree(right_pre, right_in)

        return root