
'''
7'
probably a better solution for maintaining distance between frist and second pointer
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = {}
        total = 0
        
        prev = ListNode()
        
        ans = prev
        prev.next = head
        cur = head
        
        h[0] = ans
        
        while cur:
            total += 1
            h[total] = cur
            cur = cur.next
        
        h[total-n].next = h[total-n+1].next
        
        return ans.next
            