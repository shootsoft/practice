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
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here


        if root == None:
            return node


        if node == None:
            return root

        p = root

        while p != None:
            if node.val < p.val:
                if p.left == None:
                    p.left = node
                    break
                else:
                    p = p.left
            else:

                if p.right == None:
                    p.right = node
                    break
                else:
                    p = p.right

        return root
