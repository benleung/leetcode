'''
8'
- careless: used = instead of == in condition
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        
        while cur.next != None:
            cur.val = cur.next.val
            if cur.next.next == None:
                cur.next = None
            else:
                cur = cur.next 


'''
4'38"

one take pass
'''
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
