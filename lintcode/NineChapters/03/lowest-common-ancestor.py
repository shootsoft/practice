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
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here

        if root == None or A == None or B==None:
            return
        pathA = self.getPath(root, A)
        pathB = self.getPath(root, B)

        i = 0
        j = 0
        ma = len(pathA)
        mb = len(pathB)

        print pathA
        print pathB

        while  i< ma and j<mb and pathA[i] == pathB[j]:
            result = pathA[i]
            i +=1
            j += 1

        return result

    def getPath(self, root, node):

        path = []

        while root.val != node.val:
            path.append(root.val)
            if node.val < root.val:
                root = root.left
            else:
                root = root.right

        if path == [] and root!=None and root.val == node.val:
            path.append(root.val)

        return path

s = Solution()
n = TreeNode(1)
print s.lowestCommonAncestor(n, n, n)

n1 = TreeNode(1)
n2 = TreeNode(-1)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print s.lowestCommonAncestor(n1, n2, n3).val
