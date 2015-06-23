__author__ = 'yinjun'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):

        if head == None:
            return head
        if head == None or head.next == None:
            return head
        h = ListNode(0)
        h.next = head
        n = head

        while n.next != None:

            p = n.next
            n.next = p.next

            p.next = h.next
            h.next = p


        return h.next