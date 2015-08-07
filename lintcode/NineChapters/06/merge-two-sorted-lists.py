__author__ = 'yinjun'

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        h = ListNode(0)
        p = h
        while l1!=None and l2!=None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next

        if l1!=None:
            p.next = l1

        if l2!=None:
            p.next = l2

        return h.next




