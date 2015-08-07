__author__ = 'yinjun'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        h = ListNode(0)
        l = h
        add = 0
        while l1!=None and l2!=None:
            l.next = ListNode(l1.val + l2.val + add)
            if l.next.val >= 10:
                add = 1
                l.next.val -=10
            else:
                add = 0
            l = l.next
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            l.next = ListNode(l1.val + add)
            if l.next.val >= 10:
                add = 1
                l.next.val -= 10
            else:
                add = 0
            l = l.next
            l1 = l1.next

        while l2 != None:
            l.next = ListNode(l2.val + add)
            if l.next.val >= 10:
                add = 1
                l.next.val -= 10
            else:
                add = 0
            l = l.next
            l2 = l2.next

        if add > 0:
            l.next = ListNode(add)

        return h.next
