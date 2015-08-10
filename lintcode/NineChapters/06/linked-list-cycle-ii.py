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
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here

        slow = head
        fast = head

        while slow != None and fast !=None:
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next

            if fast == slow:
                break

        if fast == None:
            return None

        slow = head
        while slow!= fast:
            slow = slow.next
            fast = fast.next

        return fast
