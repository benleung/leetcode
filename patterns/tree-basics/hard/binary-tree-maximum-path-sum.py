'''
10' revisit on 4/12
10' after knowing sol
'''
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -inf
        
        def gain(node):
            left_max = max(gain(node.left), 0) if node.left else 0
            right_max = max(gain(node.right), 0) if node.right else 0
            
            self.ans = max(self.ans, node.val + left_max + right_max)
            
            return max(node.val + left_max, node.val + right_max)
            
        gain(root)
        
        return self.ans
