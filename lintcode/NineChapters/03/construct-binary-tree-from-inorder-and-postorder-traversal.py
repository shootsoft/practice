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
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here

        if inorder == None or inorder == [] or postorder==None or postorder==[]:
            return


        root = TreeNode(postorder.pop())

        pos = inorder.index(root.val)

        if pos>0:
            root.left = self.buildTree(inorder[0:pos], postorder[0:pos])

        if pos + 1 < len(inorder):
            root.right = self.buildTree(inorder[pos+1:], postorder[pos:])


        return root