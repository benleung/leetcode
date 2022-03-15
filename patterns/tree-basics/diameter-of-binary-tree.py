'''
10' not optimal, should revisit again
'''
class Solution:
    def depth(self, root):
        left = 1 + self.depth(root.left) if root.left != None else 0
        right = 1 + self.depth(root.right) if root.right != None else 0
        return max(left, right)
        
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left = 1 + self.depth(root.left) if root.left != None else 0
        right = 1 + self.depth(root.right) if root.right != None else 0
        
        ans = left + right
        if root.left:
            ans = max(ans, self.diameterOfBinaryTree(root.left))
        if root.right:
            ans = max(ans, self.diameterOfBinaryTree(root.right))
        return ans
