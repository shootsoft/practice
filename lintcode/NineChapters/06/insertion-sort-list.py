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
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here

        if head == None or head.next == None:
            return head

        h = ListNode(0)
        h.next = head

        p = head
        while p!=None and p.next!=None:
            n = p.next
            s = h
            moved = False
            while s!=p:
                if n.val <= s.next.val:
                    p.next = p.next.next
                    n.next = s.next
                    s.next = n
                    moved = True
                    break
                else:
                    s = s.next
            if moved == False:
                p = p.next
            #print h.next

        return h.next



__author__ = 'yinjun'

'''
ListNode for lintcode and leetcode
'''
class ListNode:

    '''
    construction without parameter, default value is 0
    @:param x integer value
    '''
    def __init__(self, x):
        self.val = x
        self.next = None

    '''
    convert ListNode into list
    '''
    def toList(self):
        v = [self.val]
        c = self.next
        while c!=None:
            v.append(c.val)
            c = c.next
        return v

    '''
    convert ListNode into string
    '''
    def __str__(self):
        return str(self.toList())


    '''
    '''
    @staticmethod
    def fromList(list):
        head = ListNode(0)
        h = head
        for v in list:
            n = ListNode(v)
            h.next = n
            h = h.next

        return head.next


    @staticmethod
    def createLists(lists):
        l = []
        c = len(lists)
        for i in range(c):
            li = list(lists[i])
            lic = len(li)
            head = ListNode(0)
            chead = head
            #print lists[i]
            for j in range(lic):
                chead.next = ListNode(li[j])
                chead = chead.next
            l.append(head.next)



        return l

    @staticmethod
    def output(n):
        b = n
        print '[',
        while b != None:
            print b.val,
            b = b.next
        print ']'


s = Solution()
print s.insertionSortList(ListNode.fromList([3,2,1]))