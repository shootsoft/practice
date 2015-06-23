# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        result = []
        self.inorderTraversal2(root, result)
        return result
        
    def inorderTraversal2(self, root, result):
        
        if root == None:
            return
        self.inorderTraversal2(root.left, result)
        result.append(root.val)
        self.inorderTraversal2(root.right, result)
        
    
    