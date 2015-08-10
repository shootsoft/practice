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
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        
        if head == None or head.next == None:
            return 
        
        m = self.mid(head)
        n = self.reverse(m.next)
        m.next = None

        p = head
        while p!= None and n!=None:
            x = n.next
            n.next = p.next
            p.next = n
            n = x
            p = p.next.next



    def mid(self, head):

        slow = head
        fast = head

        while fast != None and fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head):
        h = ListNode(0)
        h.next = head
        while head!=None and head.next!=None:
            p = head.next
            head.next = p.next
            p.next = h.next
            h.next = p
        return h.next


