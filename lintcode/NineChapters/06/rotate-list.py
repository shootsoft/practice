__author__ = 'yinjun'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        l = self.lennode(head)
        if l <= 1:
            return head
            
        pos = l - k % l
        h = ListNode(0)
        h.next = head
        p = h
        i = 0
        while i < pos:
            i += 1
            p = p.next

        mid = p
        while p.next!=None:
            p = p.next
        
        last = p
        q = mid.next
        mid.next = None
        last.next = h.next
        h.next = q
        return h.next


    def lennode(self, head):

        l = 0
        h = head

        while h!=None:
            h = h.next
            l += 1

        return l