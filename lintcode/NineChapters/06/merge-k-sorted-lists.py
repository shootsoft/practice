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
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here

        if lists==None or lists==[]:
            return None

        result = []
        l = len(lists)

        if l == 1:
            return lists[0]
        elif l%2 == 0:
            for i in range(0, l, 2):
                result.append(self.merge(lists[i], lists[i+1]))
            return self.mergeKLists(result)
        else:
            for i in range(0, l-1, 2):
                 result.append(self.merge(lists[i], lists[i+1]))
            result.append(lists[l-1])
            return self.mergeKLists(result)




    def merge(self, list1, list2):

        h = ListNode(0)
        p = h

        while list1!=None and list2!=None:

            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next

            p = p.next

        if list1!=None:
            p.next = list1
        if list2!=None:
            p.next = list2

        return h.next