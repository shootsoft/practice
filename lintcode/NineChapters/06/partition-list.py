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
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        # write your code here
        h = ListNode(0)
        h.next = head
        b = None
        l = h
        p = h

        while p!= None and p.next != None:
            #print p.val, p.next.val
            if p.next.val < x and b == None:
                l = p.next
                p = p.next
            elif p.next.val >=x and b == None:
                b = p.next
                p = p.next
            elif p.next.val<x:
                n = p.next
                p.next = p.next.next
                n.next = l.next
                l.next = n
                l = n

            elif p.next.val>=x:
                n = p.next
                p.next = p.next.next
                n.next = b.next
                b.next = n
                b = n
                p = p.next
            #else:
            #    print 'sb'
            #    p = p.next
            #print h.next


        return h.next






s = Solution()
print s.partition(ListNode.fromList([3, 3, 1, 2, 4]), 3)
