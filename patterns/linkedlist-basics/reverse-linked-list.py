

'''
revisited on 4/11 (9')
revisited on 2/24 (2nd trial)
6' to solve with previous know
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = head
        if cur == None:
            return None
        nex = cur.next
        cur.next = None
        while nex != None:
            tmp = nex.next
            nex.next = cur
            cur = nex
            nex = tmp
        
        return cur


'''
revisited on 2/24
12' to solve without previous know
need some more practice
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = head
        if cur == None:
            return None
        nex = cur.next
        cur.next = None
        while nex != None:
            tmp = nex.next
            nex.next = cur
            cur = nex
            nex = tmp
        
        return cur

# 13'30"
'''
- prev, cur, nex technique is good (otherwise based on previous performance, i used took 20')
- temp can be coded faster
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        
        prev = head
        cur = head.next
        solutionHead = head
        solutionHead.next = None
        while cur:
            solutionHead = cur
            nex = cur.next
            cur.next = prev
            cur = nex
            prev = solutionHead
        return solutionHead
