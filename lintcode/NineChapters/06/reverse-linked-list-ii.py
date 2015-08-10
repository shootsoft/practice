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
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here

        h = ListNode(0)
        h.next = head

        i = 1
        p = h
        while i < m:
            i += 1
            p = p.next
       
        c = p
        last = p.next
        while i<n+1:
            q = p.next
            p.next = q.next
            q.next = c.next
            c.next = q
            p = last
            i+=1
            
            
        return h.next