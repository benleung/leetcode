'''

comment
- doesn't seem a medium question

good
- technique of dummy head is good

bad
- forget ten

learn
- carry is a better name than ten
- 

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ten = 0
        sol = ListNode()
        cur = sol
        
        nex1 = l1
        nex2 = l2
        
        while nex1 is not None or nex2 is not None or ten != 0:
            s = 0
            if nex1:
                s += nex1.val
                nex1 = nex1.next
            if nex2:
                s += nex2.val
                nex2 = nex2.next
            s += ten
            ten = s//10
            s %= 10
            
            cur.next = ListNode(s)
            cur = cur.next
        
        return sol.next
