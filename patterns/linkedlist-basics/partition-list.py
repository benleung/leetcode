'''
11'
can write even faster
'''
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        x = 3
        1 4 3 2 5 2
        
            ↑
            
        left 1
        right 4
            
        '''
        left = ListNode()
        ans = left
        right = None
        prev = ListNode()
        prev.next = head
        

        while prev.next:
            if prev.next.val < x:
                # assign to left 
                left.next = prev.next
                left = left.next
                # left.next will be overwritten

                # detach from list
                prev.next = prev.next.next
            else:
                
                if not right:
                    right = prev.next
                
                prev = prev.next
                
        
        left.next = right
        
        return ans.next
