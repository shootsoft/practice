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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here

        stack = []
        result = []
        if root == None:
            return result

        stack.append(root)
        l = 1

        while l>0:

            p = stack.pop()
            l -= 1

            result.append(p.val)

            if p.right != None:
                stack.append(p.right)
                l += 1

            if p.left != None:
                stack.append(p.left)
                l += 1



        return result

