'''
revisit on March 8, 3'
too classic and easy
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
            if slow == fast:
                return True
        return False

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        keys = set()
        cur = head
        while cur != None:
            if cur in keys:
                return True
            keys.add(cur) # not cur
            cur = cur.next
        return False
