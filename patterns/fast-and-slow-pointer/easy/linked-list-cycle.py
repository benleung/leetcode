# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
