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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        result = []
        queue = []
        if root == None:
            return result

        queue.append(root)
        l = 1

        while l>0:

            level = []

            for i in range(l):
                n = queue.pop(0)
                l-=1
                level.append(n.val)

                if n.left != None:
                    queue.append(n.left)
                    l += 1

                if n.right !=None:
                    queue.append(n.right)
                    l += 1
            #level.reverse()
            result.append(level)

        return result