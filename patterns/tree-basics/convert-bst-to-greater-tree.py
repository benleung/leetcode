'''
4'
very good understanding in recursion and post order traversal
'''
class Solution:
    def __init__(self):
        self.total = 0
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)
        
        return root
