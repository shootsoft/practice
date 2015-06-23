# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):
        d = dict()
        h = head
        
        while h != None:
            
            if h in d:
                return h
            else:
                d[h] = 1
            h = h.next
        
        return None

