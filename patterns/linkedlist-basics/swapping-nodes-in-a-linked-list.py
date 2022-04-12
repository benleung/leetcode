'''
14'
'''
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node_count = 0 
        sol_head = ListNode()
        sol_head.next = head
        prev = sol_head
        
        left_node_prev = None
        right_node_prev = None
        
        # left_node_prev, node_count are set
        while prev.next:
            node_count += 1
            
            if node_count == k:
                left_node_prev = prev
            
            prev = prev.next
        
        # right_node_prev
        right_node_number = node_count - k + 1
        prev = sol_head
        while prev.next:
            right_node_number -= 1
            if right_node_number == 0:
                right_node_prev = prev
                left_node_prev.next.val, right_node_prev.next.val = right_node_prev.next.val, left_node_prev.next.val
                break
            
            prev = prev.next
            
        
        
        return sol_head.next
