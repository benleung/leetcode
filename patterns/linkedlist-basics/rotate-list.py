'''
25'
should try to write faster
'''
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # number of node
        N = 0
        end_of_list = head # when there is at list one node, this is not None
        while True:
            N += 1
            if end_of_list.next:
                end_of_list = end_of_list.next
            else:
                break
        
        # k
        k = (N - k)%N
        # k = N - k
        if k == 0:
            return head
        
        # newheadprev
        newheadprev = ListNode() # also become end of the prev list
        newheadprev.next = head
        for _ in range(k):
            newheadprev = newheadprev.next
        newhead = newheadprev.next
        newheadprev.next = None
        end_of_list.next = head
        
        return newhead
