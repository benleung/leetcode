'''
4' after practice once already
'''

# Definition for singly-linked list.
'''
19'30"
first solution with misunderstand of q. (delete nodes from original list)
good
- realize how to use heading dummy head
bad
- slow in writing linked list

'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicates = set()
        prev = ListNode()
        dummyNode = prev  # dummyNode.next is solution
        
        cur = head
        
        while cur is not None:
            if cur.val in duplicates:
                cur = cur.next
                continue

            if cur.next is None or (cur.val != cur.next.val):
                prev.next = ListNode(cur.val)
                prev = prev.next
            else:
                duplicates.add(cur.val)

            cur = cur.next
        
        return dummyNode.next

'''
10'40"
first solution with misunderstand of q. (delete nodes from original list)

bad
- slow in writing linked list

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyFirst = ListNode(0, head)
        prev = dummyFirst
        
        duplicateVal = None
        cur = head
        
        while cur:
            if duplicateVal == cur.val:
                prev.next = cur.next
            else:
                if cur.next is None or (cur.next.val != cur.val):
                    prev = cur
                else:
                    duplicateVal = cur.val
                    prev.next = cur.next
            cur = cur.next
        return dummyFirst.next
