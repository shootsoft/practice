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
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here

        rootParent = TreeNode(0)
        rootParent.right = root

        parent = self.find(rootParent, root, value)

        if parent.left == None and parent.right==None:
            return rootParent.right
        
        node = None
        
        if parent.left!=None and parent.left.val == value:
            node = parent.left

        if parent.right!=None and parent.right.val == value:
            node = parent.right
        
        self.deleteNode(parent, node)

        return rootParent.right



    def find(self, parent, root, value):

        if root == None:
            return parent

        if root.val == value:
            return parent

        if root.val < value:
            return self.find(root, root.right, value)
        else:
            return self.find(root, root.left, value)


    def deleteNode(self, parent, node):
        
        if node == None:
            return
        
        if node.right == None:

            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left

        else:
            father = node
            temp = node.right

            while temp.left!=None:
                father = temp
                temp = temp.left


            if father.left == temp:
                father.left = temp.right
            else:
                father.right = temp.right



            if parent.left == node:
                parent.left = temp
            else:
                parent.right = temp

            temp.left = node.left
            temp.right = node.right


