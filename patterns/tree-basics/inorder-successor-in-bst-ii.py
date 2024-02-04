'''
knowledge about in-order successor -> a value just larger
dfs function for godown / goup
'''
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        target = node.val      
            
        def smallest(root):
            if not root.left:
                return root
            return smallest(root.left)
        
        # right
        right = smallest(node.right) if node.right else None
        if right:
            return right
        
        
        # parent
        while node:
            if node.val > target:
                return node
            node = node.parent
        