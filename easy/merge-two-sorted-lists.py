# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        cur = head
        i1 = l1
        i2 = l2
        while i1 != None or  i2 != None:
            if i1 != None and (i2 == None or  i1.val < i2.val):
                cur.next = ListNode(i1.val)
                i1 = i1.next
                cur = cur.next
            else:
                cur.next = ListNode(i2.val)
                i2 = i2.next
                cur = cur.next
        return head.next