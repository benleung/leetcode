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
