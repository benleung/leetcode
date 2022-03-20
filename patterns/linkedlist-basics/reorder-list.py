class Solution(object):
    
    def middleOfList(self, head):
        slow = head
        faster = head
        
        while faster and faster.next: # reach end of node or above
            faster = faster.next
            faster = faster.next
            
            if faster: # with this, left center
                slow = slow.next
        
        
        return slow
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        cur = head
        if cur == None:
            return None
        nex = cur.next
        cur.next = None
        while nex != None:
            tmp = nex.next
            nex.next = cur
            cur = nex
            nex = tmp
        
        return cur
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        middle = self.middleOfList(head)
        tail = self.reverseList(middle.next)
        middle.next = None
        
        
        
        ans = ListNode()
        cur = ans
        while head:
            # append head (# left linked list is always longer)
            cur.next = head
            head_next = head.next
            cur = cur.next
            head = head_next
            
            # append tail
            if tail:
                cur.next = tail
                tail_next = tail.next
                cur = cur.next
                tail = tail_next
        else:
            cur.next = None
        
        return ans.next
        