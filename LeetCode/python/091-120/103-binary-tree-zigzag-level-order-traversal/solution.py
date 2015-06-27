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
    @return: A list of list of integer include
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here

        result = []

        if root == None:
            return result

        queue = []
        queue.append(root)
        l = 1
        b = True

        while l >0:

            level = []
            for i in range(l):

                n = queue.pop(0)
                l -= 1

                if b:
                    level.append(n.val)
                else:
                    level.insert(0, n.val)


                if n.left!=None:
                    queue.append(n.left)
                    l+=1

                if n.right!=None:
                    queue.append(n.right)
                    l+=1
            b = not b
            result.append(level)


        return result