'''
1 hr but cannot figure out solution

'''

class Solution:
    def __init__(self):
        self.nodes = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        if head in self.nodes:
            return self.nodes[head]
        
        node = Node(x = head.val)
        self.nodes[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
        