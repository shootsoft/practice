__author__ = 'yinjun'

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here

        result = []
        result.append(self.preorderTraversal(root))
        result.append(self.inorderTraversal(root))
        return result


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

    def preorderTraversal(self, root):
        # write your code here

        stack = []
        result = []
        if root == None:
            return result

        stack.append(root)
        l = 1

        while l>0:

            p = stack.pop()
            l -= 1

            result.append(p.val)

            if p.right != None:
                stack.append(p.right)
                l += 1

            if p.left != None:
                stack.append(p.left)
                l += 1



        return result

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here

        if data==None or data == [] or len(data)!=2:
            return None

        return self.buildTree(data[0], data[1])


    def buildTree(self, preorder, inorder):
        # write your code here
        if preorder ==[] and inorder == []:
            return None

        root = TreeNode(preorder[0])

        inpos = inorder.index(preorder[0])

        if inpos>0:
            left_pre = preorder[1:inpos+1]
            left_in = inorder[0:inpos]
            root.left = self.buildTree(left_pre, left_in)

        length = len(inorder)

        if  inpos + 1 < length:

            right_pre = preorder[inpos+1:]
            right_in = inorder[inpos+1:]
            root.right = self.buildTree(right_pre, right_in)

        return root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.left = n2
n2.left = n3
n3.left = n4
print s.serialize(n1)
#print s.serialize(n1)
#print s.serialize(s.deserialize([1, '#', 2]))
#print s.serialize(s.deserialize([1,2,3,'#','#',4,5]))
#print s.serialize(s.deserialize([1, 2, '#', 3, '#',4]))