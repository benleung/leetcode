
''''
40' qucick sort
tle
'''
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def quicksort(head): # [head or list, tail of list]
            if not head:
                return [None, None]

            pivot = head
            prev = head
            big = ListNode()
            big_head = big
            small = ListNode()
            small_head = small

            while prev.next:
                if prev.next.val < pivot.val:
                    small.next = prev.next
                    prev = prev.next
                    small = small.next
                    big.next = None

                else:
                    big.next = prev.next
                    prev = prev.next
                    big = big.next
                    small.next = None

            small_head, small_tail = quicksort(small_head.next)
            big_head, big_tail = quicksort(big_head.next)
                    
            root = ListNode()
            tail = root
            
            # small
            if small_head and small_tail:
                tail.next = small_head
                tail = small_tail
            
            # pivot
            tail.next = pivot # impossible to be None
            tail = pivot
            
            # big
            if big_head and big_tail:
                tail.next = big_head
                tail = big_tail
            
            tail.next = None

            return [root.next, tail]
        
        return quicksort(head)[0]
