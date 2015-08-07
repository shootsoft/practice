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
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        h = ListNode(0)
        h.next = head
        while head!=None and head.next!=None:
            p = head.next
            head.next = p.next
            p.next = h.next
            h.next = p
        return h.next

