
'''
not fast enough to write while loop
linkedlist loop detection skills need revision
'''
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        
        if not head:
            ans = node
            ans.next = ans
            return ans
        
        # find the max node, assign it to cur
        cur = head
        max_val = head.val
        while cur.next.val >= max_val and cur.next != head :  # avoid infinite loop
            max_val = cur.next.val
            cur = cur.next
        
        # find insertVal is the largest value
        if insertVal >= max_val:
            nex = cur.next
            cur.next = node
            cur.next.next = nex
            return head
        
        # find the 
        while not(insertVal <= cur.next.val):
            cur = cur.next
        else:
            nex = cur.next
            cur.next = node
            cur.next.next = nex
        
        return head
        