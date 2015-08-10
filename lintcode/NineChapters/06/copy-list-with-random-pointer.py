__author__ = 'yinjun'

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        dict= {}
        p = head
        c = RandomListNode('')
        m = c
        while p != None:
            q = RandomListNode(p.label)
            dict[p] = q
            m.next = q
            p = p.next
            m = m.next
            
        p = head
        q = c.next
        while q != None:
            if p.random in dict:
                q.random = dict[p.random]
            q = q.next
            p = p.next

        return c.next
