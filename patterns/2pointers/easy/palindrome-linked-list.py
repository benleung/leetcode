'''
17' (actually medium difficulty)

- reverse link list
- trick to reach the medium point of the list use fast & slow pointer
- xxx.next = xxxx will modify the link list, while transversal doesn't
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        count //= 2
        
        secondHalf = head
        for i in xrange(0, count):
            secondHalf = secondHalf.next
        # secondHalf is now in the middle
        rev = self.reverseList(secondHalf)
        
        
        while head != None and rev != None and count>0:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
            count -= 1
        return True
        
    def reverseList(self, head):
        prev = None
        cur = head
        while cur != None:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev
        