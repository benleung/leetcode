'''
19'

good
- learn the technique of expanding and perform a specific actions at each level

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

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque([root])
        
        while queue:
            # assign next (specific action for this depth)
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
            nextQueue = []
            for _ in range(len(queue)): #technique to append a list of nodes for next depth
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return root
