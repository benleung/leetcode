'''
consider this as recursion instead of backtracking would be easier to understand
be careful about returning cur.val or return cur
'''
class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def recurse_tree(cur):
            if not cur:
                return False 
            mid = cur.val == p.val or cur.val == q.val
            left = recurse_tree(cur.left)
            right = recurse_tree(cur.right)
            if (mid and left) or (mid and right) or (left and right):
                self.ans = cur
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans
                
'''
1hr
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        
        def findPath(val):
            stack = [(root, [])]
            while stack:
                (node, path) = stack.pop()
                path = path + [node]
                if node.val == val:
                    return path
                if node.left:
                    stack.append((node.left, path))
                if node.right:
                    stack.append((node.right, path))
        
        pPath = findPath(p.val)
        qPath = findPath(q.val)
        
        for i in range(min(len(pPath), len(qPath))):
            if pPath[i].val != qPath[i].val:
                return pPath[i-1]
        else:
            return pPath[min(len(pPath), len(qPath)) - 1]
                
        
        
