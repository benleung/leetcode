'''
33' should practice to do faster
pass the solutin one time is good
'''
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # if only one node
        if head.next == None or left == right:
            return head
        
        # if left == 1
        
        node = ListNode()
        ans = node
        node.next = head
        
        for _ in range(1,left):
            node = node.next
        # node.next is the first node that requires reversing
        start = node  # start.next is kept
        
        prev = None
        node = node.next
        for _ in range(right - left+1):
            nex = node.next
            node.next = prev
            prev = node
            node = nex
        
        start.next.next = node
        start.next = prev
        
        return ans.next
