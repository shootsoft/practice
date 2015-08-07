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
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        # write your code here

        l = self.nodelen(head)
        i = 0
        m = head
        while i<l-n and m!=None:
            m = m.next
            i+= 1

        return m

    def nodelen(self, head):
        h = head
        l = 0
        while h != None:
            l += 1
            h = h.next
        return l