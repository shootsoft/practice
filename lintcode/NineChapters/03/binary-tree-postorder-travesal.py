__author__ = 'yinjun'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):

        stack = []
        dict = {}
        result = []

        if root == None:
            return result

        stack.append(root)
        if root.right!=None:
            stack.append(root.right)
        if root.left!=None:
            stack.append(root.left)
        l = len(stack)

        while l>0:
            #print result
            p = stack.pop()
            l -= 1
            if p.left ==None and p.right ==None or \
               p.right != None and p.right in dict or \
               p.left !=None and p.right==None and p.left in dict or \
               p.left != None and p.right!=None and p.left in dict and p.right in dict:
                dict[p] = 1
                result.append(p.val)
            else:
                stack.append(p)
                if p.right!=None:
                    stack.append(p.right)
                if p.left!=None:
                    stack.append(p.left)
                l = len(stack)

        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3

s = Solution()
print s.postorderTraversal(n1)