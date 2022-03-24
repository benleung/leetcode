'''
7' -> 5' (revisited on march 23)

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q  =deque([root])
        while len(q) > 0:
            prev = None
            for _ in range(len(q)):
                node = q.pop()
                node.next = prev
                prev = node
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)
        return root


'''
10'

<learn>
revise skill to tranverse each layer
  for _ in len(q):   loop
deque order
  queue
    appendleft(right) --> imagine right comes out first
    appendleft(left)
    pop() # not popleft
    pop()
  stack
    append(left) --> imagine left comes out last
    append(right)
    pop
nex = None
  temp save, and then replace later


<careless mistake>
  - if xxx.right: q.append(xxx.right)
  - deque([root])  # root can be None
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        
        q = deque([root])
        nex = None
        while q:
            for _ in range(len(q)):
                p = q.pop()
                p.next = nex
                nex = p
                if p.right:
                    q.appendleft(p.right)
                if p.left:
                    q.appendleft(p.left)
            nex = None
        return root
