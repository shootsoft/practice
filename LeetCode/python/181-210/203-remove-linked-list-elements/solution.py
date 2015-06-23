__author__ = 'yinjun'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):

        h = ListNode(0)
        h.next = head
        n = h


        while n.next != None:
            c = n.next
            if c.val == val:
                n.next = c.next
            else:
                n = n.next


        return h.next
