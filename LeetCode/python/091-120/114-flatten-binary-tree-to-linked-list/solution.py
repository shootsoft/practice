__author__ = 'yinjun'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        node = root
        self.flattenHelp(node)


    def flattenHelp(self, node):

        if node == None:
            return
        left = node.left
        right = node.right
        node.left = None
        if left:
            node.right = left
            node = node.right
            self.flattenHelp(node)
        if right:
            node.right = right
            node = node.right
            self.flattenHelp(node)
        