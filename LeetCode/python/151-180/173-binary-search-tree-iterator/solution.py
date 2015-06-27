__author__ = 'yinjun'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):

        stack = []
        dict = {}
        dictStack = {}
        self.result = []
        self.length = 0
        self.pos = 0
        if root == None:
            return

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
                self.result.append(p.val)
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

        self.length = len(self.result)
        #return self.result

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.pos < self.length

    # @return an integer, the next smallest number
    def next(self):
        p = self.result[self.pos]
        self.pos += 1
        return p

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())