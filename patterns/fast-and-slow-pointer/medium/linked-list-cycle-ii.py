'''
less than 10'

there is another algorithm (Floyd's Tortoise and Hare) that might be a followup question
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        keys = set()
        prev = ListNode()
        prev.next = head
        while prev.next:
            if prev.next in keys:
                return prev.next
            else:
                keys.add(prev.next)
                prev = prev.next
        return None
