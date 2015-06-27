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
        queue =[]
        if root == None:
            return result

        queue.append(root)
        l = 1

        while l > 0:

            hasNext = False

            for i in range(l):
                #print i
                if  queue[i]!='#' and (queue[i].left !=None or queue[i].right !=None):
                    hasNext = True
                    break
            #print hasNext
            for i in range(l):

                p = queue.pop(0)
                l -= 1
                if p == '#':
                    result.append('#')
                    if hasNext:
                        queue.append('#')
                        queue.append('#')
                else:
                    result.append(p.val)

                    if p.left != None:
                        queue.append(p.left)
                    elif hasNext:
                         queue.append('#')

                    if p.right !=None:
                        queue.append(p.right)
                    elif hasNext:
                        queue.append('#')

                l = len(queue)
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

        if data == None or data==[]:
            return None

        length = len(data)
        pos = 1
        level = 2
        root = TreeNode(data[0])
        queue = [root]

        while pos < length:
            #print pos,  2**(level-1) + 1
            for i in range(pos, 2**(level-1) + 1, 2):
                if i> length:
                    break
                pos += 2
                #print 'i =', i
                p = queue.pop(0)
                if p != None:
                    #print 'p.val =',p.val
                    #print i
                    if data[i] == '#':
                        queue.append(None)
                    else:
                        p.left = TreeNode(data[i])
                        queue.append(p.left)
                        #print 'left =', data[i]

                    if data[i+1] == '#':
                        queue.append(None)
                    else:
                        p.right = TreeNode(data[i + 1])
                        queue.append(p.right)
                        #print 'right =', data[i + 1]
                else:
                    queue.append(None)
                    queue.append(None)
            #pos += 2**(level-1) + 1
            level += 1
            #print 'pos =', pos

        return root

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n1.right = n2
#print s.serialize(n1)
#print s.serialize(s.deserialize([1, '#', 2]))
#print s.serialize(s.deserialize([1,2,3,'#','#',4,5]))
print s.serialize(s.deserialize([1, 2, '#', 3, '#',4]))