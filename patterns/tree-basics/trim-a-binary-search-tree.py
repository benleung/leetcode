class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        #  lowest: leftmost
        #  highest: rightmost
        
        if root.val < low:
            if not root.right:
                return None
            else:
                return self.trimBST(root.right, low, high)
        
        
        if root.val > high:
            if not root.left:
                return None
            else:
                return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high) if root.left else None
        root.right = self.trimBST(root.right, low, high) if root.right else None
        return root
