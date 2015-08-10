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
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here

        if head == None or head.next==None:
            return head

        m = self.mid(head)
        n = m.next
        m.next = None
        return self.merge(self.sortList(head), self.sortList(n))

    def mid(self, head):

        slow = head
        fast = head

        while fast.next!= None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next

        return slow


    def merge(self, a, b):

        h = ListNode(0)
        p = h
        while a!=None and b!=None:
            if a.val < b.val:
                p.next = a
                a = a.next
            else:
                p.next = b
                b = b.next
            p = p.next

        if a!=None:
            p.next = a
        if b!=None:
            p.next = b
        return h.next