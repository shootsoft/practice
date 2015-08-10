# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        l = len(nums)
        if l==0:
            return None
        elif l == 1:
            return TreeNode(nums[0])
        elif l==2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        else:
            p = l/2
            root = TreeNode(nums[p])
            root.left = self.sortedArrayToBST(nums[0:p])
            root.right = self.sortedArrayToBST(nums[p+1:])
            return root