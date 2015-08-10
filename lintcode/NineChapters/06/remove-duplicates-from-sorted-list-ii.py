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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        delete = {}
        h = ListNode(0)
        h.next = head
        p = h
        while p!=None and p.next!=None and p.next.next!=None:
            if p.next.val == p.next.next.val:
                delete[p.next.val] = True
                p.next = p.next.next
            elif p.next.val in delete:
                p.next = p.next.next
            else:
                p = p.next

        if p!=None and p.next!=None and p.next.val in delete:
            p.next = None

        return h.next

