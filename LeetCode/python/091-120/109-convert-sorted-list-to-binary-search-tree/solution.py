# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        nums = []
        while head!=None:
            nums.append(head.val)
            head = head.next
        
        return self.sortedArrayToBST(nums)
        
        
    def sortedArrayToBST(self, nums):
        
        l = len(nums)
        if l ==0:
            return None
        elif l == 1:
            return TreeNode(nums[0])
        elif l ==2:
            root = TreeNode(nums[0])
            root.right = TreeNode(nums[1])
            return root
        else:
            mid = l/2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[0:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root
