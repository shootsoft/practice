# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        result =[]
        if root == None :
            return result
        
        queue = []
        queue.append(root)
        
        while(len(queue)>0):
            cur = []
            l = len(queue)
            while l > 0:
                n = queue.pop(0)
                cur.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
                l -= 1
            result.append(cur)
        
        result.reverse()
        return result
                
        
        