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



__author__ = 'yinjun'

'''
ListNode for lintcode and leetcode
'''
class ListNode:

    '''
    construction without parameter, default value is 0
    '''
    def __init__(self):
        self.val = 0
        self.next = None

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

    '''
    convert ListNode into string
    '''
    def __str__(self):
        self.toLit()
        return str(lst)


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
print s.partition(ListNode.fromList([3, 3, 1, 2, 4]), 3)
