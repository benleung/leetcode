class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        sol = None  #head
        prev = head
        while prev != None:
            if prev.val != val:
                sol = prev # def solution head here
                break
            prev = prev.next
        
        while prev is not None and prev.next is not None:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
                    
        return sol
