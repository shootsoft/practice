__author__ = 'yinjun'

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None

Example of iterate a tree:
iterator = Solution(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
class Solution:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here

        self.stack = []
        self.dict = {}
        self.dictStack = {}

        if root == None:
            return

        if root.right!=None:
            self.stack.append(root.right)
            self.dictStack[root.right] = 1
        self.stack.append(root)
        self.dictStack[root] = 1
        if root.left!=None:
            self.stack.append(root.left)
            self.dictStack[root.left] = 1
        self.length = len(self.stack)

    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        while self.length > 0:


            p = self.stack.pop()
            self.dictStack.pop(p)
            self.length -= 1

            if p.left ==None or p.left !=None and p.left in self.dict:
                self.dict[p] = 1
                self.next = p
                #result.append(p.val)
                if p.right!=None and p.right not in self.dictStack:
                   self.stack.append(p.right)
                   self.dictStack[p.right] = 1
                   self.length += 1

                return True
            else:
                if p.right!=None:
                    self.stack.append(p.right)
                    self.dictStack[p.right] = 1
                self.stack.append(p)
                self.dictStack[p] = 1
                if p.left!=None:
                    self.stack.append(p.left)
                    self.dictStack[p.left] = 1
                self.length = len(self.stack)

        return False




    #@return: return next node
    def next(self):
        #write your code here

        return self.next
