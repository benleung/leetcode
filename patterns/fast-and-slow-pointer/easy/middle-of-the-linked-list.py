'''
revist on 12/11: 4'50": 
by thinking about case of 3 element and case of 4 element


already record in anki
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        faster = head
        
        while faster and faster.next: # reach end of node or above
            faster = faster.next
            faster = faster.next
            
            slow = slow.next
        
        
        return slow


'''
second trial with same result: 4'10"
'''
