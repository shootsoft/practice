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
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here

        if head == None or head.next == None:
            return False

        slow = head
        fast = head

        while fast.next != None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

