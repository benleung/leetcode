# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = ListNode(0)
        ans = prev
        prev.next = head
        cur = head
        nex = cur.next
        
        while cur and nex:
            prev.next = nex
            cur.next = nex.next
            nex.next = cur
            
            prev = cur
            cur = cur.next
            if cur:
                nex = cur.next
        
        return ans.next
