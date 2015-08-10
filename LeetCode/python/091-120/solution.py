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

        return self.buildTreeHelp(preorder, 0, inorder, 0, len(inorder))



    def buildTreeHelp(self, preorder, prestart, inorder, instart, length):

        root = TreeNode(preorder[prestart])
        
        inpos = inorder.index(preorder[prestart], instart)

        if inpos>0:
            left_pre_start = prestart + 1  #preorder[1:inpos+1]
            left_in_start = instart #inorder[0:inpos]
            left_len = inpos - instart #inorder[0:inpos]
            
            root.left = self.buildTreeHelp(preorder, left_pre_start, inorder, left_in_start, left_len)

        

        if  inpos + 1 < length + instart:

            right_pre_start = inpos+1 #preorder[inpos+1:]
            right_in_start = inpos+1 #inorder[inpos+1:]
            right_len = length + instart - inpos
            root.right = self.buildTreeHelp(preorder, right_pre_start, inorder, right_in_start, right_len)

        return root