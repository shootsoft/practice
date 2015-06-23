# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        d = dict()
        h = head
        
        while h != None:
            
            if h in d:
                return True
            else:
                d[h] = 1
            h = h.next
        
        return False


#another
# class Solution:
#     # @param head, a ListNode
#     # @return a boolean
#     def hasCycle(self, head):
#         if not head:
#             return False
#
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow is fast:
#                 return True
#
#         return False