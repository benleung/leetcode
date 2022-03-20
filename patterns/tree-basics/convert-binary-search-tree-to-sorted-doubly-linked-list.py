'''
30'

bad
- slow in writing doubly linked list
'''
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def dfs(root): # left, right
            # root cannot be None
            head = Node()
            cur = head
            if root.left:
                l, r = dfs(root.left)
                cur.right = l
                # l.left = head
                cur = r
            
            # right_tmp = root.right
            cur.right = root
            root.left = cur
            cur = root
            
            if root.right:
                l, r = dfs(root.right)
                cur.right = l
                l.left = cur
                cur = r
            
            cur.right = None
            head.right.left = None
            
            return (head.right, cur)
            
        if not root:
            return None
        
        # what happen if only one node
        # create cycle
        left, right = dfs(root)
        
        left.left = right
        right.right = left
        
        return left
