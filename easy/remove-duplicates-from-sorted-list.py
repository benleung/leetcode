# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         cur = head
        
#         while cur != None and cur.next != None:
#             nex = cur.next
#             while nex != None and cur.val == nex.val:
#                 nex = nex.next
#             cur.next = nex
#             cur = cur.next
        
#         return head
# almost 20 minutes to solve

# 5' to solve which dummy first node technique
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sol = ListNode(None)
        sol.next = head
        prev, cur = sol, sol.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
                
        return sol.next
