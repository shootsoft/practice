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
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):


        if root == None or root.left == None and root.right == None:
            return True
        else:

            if root.left!=None and root.right!=None and root.left.val < root.val and root.right.val > root.val:


                return self.isValidBST(root.left) and self.checkMaxNode(root.left, root.val) \
                       and self.isValidBST(root.right) and self.checkMinNode(root.right, root.val)
            elif root.left!=None and root.right == None and root.left.val < root.val:
                 return self.isValidBST(root.left) and self.checkMaxNode(root.left, root.val)
            elif root.right!=None and root.left == None and root.right.val > root.val:
                return self.isValidBST(root.right) and self.checkMinNode(root.right, root.val)
            else:
                return False
    
    def checkMaxNode(self, root, max):
        
        if root == None:
            return True
        else:
            return root.val < max and self.checkMaxNode(root.left, max) and self.checkMaxNode(root.right, max)
            
    def checkMinNode(self, root, min):
        
        if root == None:
            return True
        else:
            return root.val > min and self.checkMinNode(root.left, min) and self.checkMinNode(root.right, min)


