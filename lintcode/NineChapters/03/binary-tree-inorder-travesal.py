__author__ = 'yinjun'

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here

        stack = []
        dict = {}
        dictStack = {}
        result = []

        if root == None:
            return result

        if root.right!=None:
            stack.append(root.right)
            dictStack[root.right] = 1
        stack.append(root)
        dictStack[root] = 1
        if root.left!=None:
            stack.append(root.left)
            dictStack[root.left] = 1
        l = len(stack)

        while l>0:
            #print result
            p = stack.pop()
            dictStack.pop(p)
            l -= 1
            if p.left ==None or p.left !=None and p.left in dict:
                dict[p] = 1
                result.append(p.val)
                if p.right!=None and p.right not in dictStack:
                   stack.append(p.right)
                   dictStack[p.right] = 1
                   l += 1
            else:
                if p.right!=None:
                    stack.append(p.right)
                    dictStack[p.right] = 1
                stack.append(p)
                dictStack[p] = 1
                if p.left!=None:
                    stack.append(p.left)
                    dictStack[p.left] = 1
                l = len(stack)

        return result

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3

s = Solution()
print s.inorderTraversal(n1)