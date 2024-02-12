'''
revisit on 2024/2/12 13'
5'
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        prev = head
        while l1 != None and  l2 != None:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
            
        return head.next

'''
should write with O(1) space
need practice
'''
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
