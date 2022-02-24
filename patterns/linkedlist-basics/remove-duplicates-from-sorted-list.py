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

'''
8' to solve for second time, but still not smooth enough
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sol = ListNode()
        sol.next = head
        prev = sol
        
        while prev.next and prev.next.next:
            if prev.next.val == prev.next.next.val:
                prev.next = prev.next.next #removed
            else:
                prev = prev.next
                
        
        return sol.next
