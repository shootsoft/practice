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
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here

        if head == None:
            return head

        pre = ListNode(0)
        pre.next = head
        p = pre
        l = self.nodelen(head)

        for i in range(l-n):
            if pre.next != None:
                pre = pre.next
            else:
                return head

        if pre.next!=None and pre.next.next!=None:
            pre.next = pre.next.next
        else:
            pre.next = None
        return p.next

    def nodelen(self, head):

        h = head
        l = 0

        while h != None:
            l += 1
            h = h.next

        return l

