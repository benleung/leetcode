'''
8'
'''
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        
        def findDepthTree(depth, r):
            if not r:
                return
            self.max_depth = max(self.max_depth, depth)
            findDepthTree(depth+1, r.left)
            findDepthTree(depth+1, r.right)
            
        findDepthTree(0, root) # max_depth is updated
        
        self.ans = 0
        def leavesSum(depth, node): # node is non-null
            if depth == self.max_depth:
                self.ans += node.val
            
            if node.left:
                leavesSum(depth+1, node.left)
            if node.right:
                leavesSum(depth+1, node.right)
        
        leavesSum(0, root)
        return self.ans
            